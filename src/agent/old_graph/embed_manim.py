import os
import re
from pathlib import Path
from typing import List, Optional, Dict, Any

from dotenv import load_dotenv

from openai import OpenAI
from langchain_core.embeddings import Embeddings
from langchain_core.documents import Document

from qdrant_client import QdrantClient
from qdrant_client.http import models as qm

from langchain_qdrant import QdrantVectorStore, FastEmbedSparse, RetrievalMode
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

# Toggle this when you want to rebuild the index from markdown
# Set to True the first time you build the new Qwen3 based collection
REBUILD_INDEX = False

# -------------------------------------------------------------------
# Dense embeddings with Qwen3 via OpenRouter
# -------------------------------------------------------------------
class OpenRouterQwen3Embeddings(Embeddings):
    """
    LangChain Embeddings wrapper for OpenRouter qwen/qwen3-embedding-8b.

    Uses OPENROUTER_API_KEY from env.
    """

    def __init__(
        self,
        model: str = "qwen/qwen3-embedding-8b",
        api_key: Optional[str] = None,
        site_url: Optional[str] = None,
        site_title: Optional[str] = None,
    ):
        self.model = model
        self.api_key = api_key or os.environ.get("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY is not set in env")

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.api_key,
        )

        # These headers are recommended by OpenRouter for routing and analytics
        self.extra_headers: Dict[str, str] = {}
        if site_url:
            self.extra_headers["HTTP-Referer"] = site_url
        if site_title:
            self.extra_headers["X-Title"] = site_title

    def _embed(self, texts: List[str]) -> List[List[float]]:
        if not texts:
            return []
        resp = self.client.embeddings.create(
            model=self.model,
            input=texts,
            encoding_format="float",
            extra_headers=self.extra_headers or None,
        )
        data = getattr(resp, "data", None)
        if not data:
            raise RuntimeError(f"OpenRouter embedding call returned no data: {resp}")
        return [item.embedding for item in data]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self._embed(texts)

    def embed_query(self, text: str) -> List[float]:
        return self._embed([text])[0]


# -------------------------------------------------------------------
# Helpers for metadata from file paths and headings
# -------------------------------------------------------------------
def build_base_metadata_from_path(rel_path: str) -> Dict[str, Any]:
    meta: Dict[str, Any] = {"file_path": rel_path}

    m = re.search(r"docs\.manim\.([^_]+(?:_[^_]+)*)_reference_", rel_path)
    if m:
        meta["version"] = m.group(1)

    path_no_root = rel_path
    if "manim_docs/" in rel_path:
        path_no_root = rel_path.split("manim_docs/", 1)[1]

    if path_no_root.startswith("docs.manim."):
        path_no_root = path_no_root[len("docs.manim.") :]

    if "reference_" in path_no_root:
        path_no_root = path_no_root.split("reference_", 1)[1]

    if path_no_root.endswith(".html.md"):
        path_no_root = path_no_root[: -len(".html.md")]

    qualified_from_path = path_no_root
    meta["qualified_name_from_path"] = qualified_from_path

    parts = qualified_from_path.split(".") if qualified_from_path else []
    if len(parts) > 1:
        meta["module"] = ".".join(parts[:-1])
        meta["symbol_name_from_path"] = parts[-1]
    elif parts:
        meta["module"] = parts[0]
        meta["symbol_name_from_path"] = None
    else:
        meta["module"] = None
        meta["symbol_name_from_path"] = None

    return meta


def clean_heading_symbol(symbol_header: Optional[str]) -> Optional[str]:
    if not symbol_header:
        return None
    cleaned = symbol_header.split("[", 1)[0].strip()
    return cleaned or None


def infer_symbol_kind_from_content(content: str, symbol_name: Optional[str]) -> str:
    head = content[:1500]
    head_lower = head.lower()

    if symbol_name:
        sn = symbol_name
        sn_lower = sn.lower()
        if f"_class_ {sn_lower}" in head_lower or f"class {sn}(" in head:
            return "class"
        if "_function_" in head_lower or f"{sn}(" in head:
            return "function_or_method"

    if "mobjects representing" in head_lower:
        return "module"
    if "utilities to create and set the logger".lower() in head_lower:
        return "module"
    if "qualified name:" in head_lower:
        return "symbol"

    return "section"


def refine_symbol_metadata(
    base_meta: Dict[str, Any],
    header_symbol: Optional[str],
    content: str,
) -> Dict[str, Any]:
    meta = dict(base_meta)

    path_qualified = meta.get("qualified_name_from_path")
    module = meta.get("module")
    base_symbol_from_path = meta.get("symbol_name_from_path")

    symbol_name = clean_heading_symbol(header_symbol) or base_symbol_from_path

    if symbol_name and module:
        if path_qualified and path_qualified.endswith("." + symbol_name):
            qualified = path_qualified
        else:
            qualified = f"{module}.{symbol_name}"
    else:
        qualified = path_qualified or symbol_name

    meta["symbol_name"] = symbol_name
    meta["qualified_name"] = qualified
    meta["symbol_kind"] = infer_symbol_kind_from_content(content, symbol_name)

    return meta


# -------------------------------------------------------------------
# Load unified markdown and turn into header-level Documents
# -------------------------------------------------------------------
def load_manim_docs_from_unified(
    unified_path: Path,
) -> List[Document]:
    text = unified_path.read_text(encoding="utf-8")

    doc_start_pattern = re.compile(r"<!-- DOC START: (.*?) -->")
    doc_start_matches = list(doc_start_pattern.finditer(text))

    if doc_start_matches:
        boundaries = []
        for i, match in enumerate(doc_start_matches):
            rel_path = match.group(1).strip()
            start = match.end()
            end = (
                doc_start_matches[i + 1].start()
                if i + 1 < len(doc_start_matches)
                else len(text)
            )
            boundaries.append((rel_path, start, end))
    else:
        heading_pattern = re.compile(
            r"^#\s+(manim_docs/[^\n]+)$",
            flags=re.MULTILINE,
        )
        heading_matches = list(heading_pattern.finditer(text))
        if not heading_matches:
            raise RuntimeError(
                f"No DOC START markers and no '# manim_docs/...' headings found in {unified_path}. "
                "Check the format of the unified markdown file."
            )

        boundaries = []
        for i, match in enumerate(heading_matches):
            rel_path = match.group(1).strip()
            start = match.start()
            end = (
                heading_matches[i + 1].start()
                if i + 1 < len(heading_matches)
                else len(text)
            )
            boundaries.append((rel_path, start, end))

    md_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "file"),
            ("##", "symbol"),
            ("###", "subsection"),
        ]
    )

    all_docs: List[Document] = []

    for rel_path, start, end in boundaries:
        doc_block = text[start:end]

        end_marker_index = doc_block.find("<!-- DOC END -->")
        if end_marker_index != -1:
            doc_block = doc_block[:end_marker_index]

        header_chunks = md_splitter.split_text(doc_block)
        base_meta = build_base_metadata_from_path(rel_path)

        for ch in header_chunks:
            meta = dict(base_meta)

            header_file = ch.metadata.get("file")
            header_symbol = ch.metadata.get("symbol")
            header_subsection = ch.metadata.get("subsection")

            if header_file:
                meta["file_header"] = header_file
            if header_symbol:
                meta["heading_symbol"] = header_symbol
            if header_subsection:
                meta["heading_subsection"] = header_subsection

            meta = refine_symbol_metadata(
                base_meta=meta,
                header_symbol=header_symbol,
                content=ch.page_content,
            )

            all_docs.append(
                Document(
                    page_content=ch.page_content,
                    metadata=meta,
                )
            )

    return all_docs


# -------------------------------------------------------------------
# Second level chunking - now 800 chars with 200 overlap
# -------------------------------------------------------------------
def chunk_docs(
    docs: List[Document],
    chunk_size: int = 1600,
    chunk_overlap: int = 200,
) -> List[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""],
    )
    return splitter.split_documents(docs)


# -------------------------------------------------------------------
# Hybrid Qdrant store with payload indexing
# -------------------------------------------------------------------
def build_manim_vector_store(
    client: QdrantClient,
    collection_name: str,
    docs: List[Document],
) -> QdrantVectorStore:
    dense_embeddings = OpenRouterQwen3Embeddings()
    sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")

    vector_store = QdrantVectorStore.from_documents(
        documents=docs,
        embedding=dense_embeddings,
        sparse_embedding=sparse_embeddings,
        url=os.environ["QDRANT_URL"],
        api_key=os.environ.get("QDRANT_API_KEY"),
        prefer_grpc=False,
        collection_name=collection_name,
        retrieval_mode=RetrievalMode.HYBRID,
        force_recreate=True,
    )

    index_fields = [
        "file_path",
        "module",
        "symbol_name",
        "symbol_kind",
        "qualified_name",
        "version",
    ]

    for field in index_fields:
        try:
            client.create_payload_index(
                collection_name=collection_name,
                field_name=field,
                field_schema=qm.PayloadSchemaType.KEYWORD,
            )
            print(f"Created payload index on '{field}'")
        except Exception as e:
            print(f"Skipping index on '{field}': {e}")

    return vector_store


# -------------------------------------------------------------------
# Example main for rebuilding the index only
# -------------------------------------------------------------------
def main() -> None:
    load_dotenv()

    collection_name = "manim_docs_qwen3_embed_8b_1600_200"

    if not REBUILD_INDEX:
        print("REBUILD_INDEX is False, nothing to do. Set it to True to rebuild the index.")
        return

    qdrant_client = QdrantClient(
        url=os.environ["QDRANT_URL"],
        api_key=os.environ.get("QDRANT_API_KEY"),
    )

    root = Path(__file__).resolve().parent
    unified_path = root / "unified_manim_community_docs.md"

    if not unified_path.is_file():
        raise FileNotFoundError(
            f"Unified docs file not found at {unified_path}. "
            "Make sure your stitching script has created it."
        )

    print("Loading unified Manim markdown and creating Documents...")
    docs = load_manim_docs_from_unified(unified_path)
    print(f"Loaded {len(docs)} header level document chunks")

    docs = chunk_docs(docs, chunk_size=1600, chunk_overlap=200)
    print(f"After secondary chunking: {len(docs)} chunks")

    print("Building Qdrant hybrid vector store (Qwen3 embeddings)...")
    build_manim_vector_store(
        client=qdrant_client,
        collection_name=collection_name,
        docs=docs,
    )
    print("Index rebuild complete.")


if __name__ == "__main__":
    main()
