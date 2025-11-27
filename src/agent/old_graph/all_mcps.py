# all_mcps.py - Unified MCP server aggregating multiple MCP tools

import os
from typing import List

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from langchain_qdrant import QdrantVectorStore, FastEmbedSparse, RetrievalMode
from langchain_core.documents import Document
import requests

from embed_manim import OpenRouterQwen3Embeddings  # your index builder file

load_dotenv()

mcp = FastMCP("ManimDocs")

VOYAGE_API_KEY = os.environ.get("VOYAGEAI_API_KEY")
QDRANT_URL = os.environ.get("QDRANT_URL")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")

if not VOYAGE_API_KEY:
    raise RuntimeError("VOYAGEAI_API_KEY is not set")
if not QDRANT_URL:
    raise RuntimeError("QDRANT_URL is not set")

COLLECTION_NAME = "manim_docs_qwen3_embed"

dense_embeddings = OpenRouterQwen3Embeddings()
sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")

vector_store = QdrantVectorStore.from_existing_collection(
    collection_name=COLLECTION_NAME,
    embedding=dense_embeddings,
    sparse_embedding=sparse_embeddings,
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    prefer_grpc=False,
    retrieval_mode=RetrievalMode.HYBRID,
)


def rerank_docs(query: str, docs: List[Document], top_k: int = 6) -> List[Document]:
    if not docs:
        return []

    contents = [d.page_content for d in docs]

    resp = requests.post(
        "https://api.voyageai.com/v1/rerank",
        headers={
            "Authorization": f"Bearer {VOYAGE_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "rerank-2.5-lite",
            "query": query,
            "documents": contents,
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()["data"]

    scores = {item["index"]: item["relevance_score"] for item in data}
    ranked = sorted(
        enumerate(docs),
        key=lambda pair: scores.get(pair[0], 0.0),
        reverse=True,
    )
    return [docs[idx] for idx, _ in ranked[:top_k]]


@mcp.tool()
def manim_docs_search(
    query: str,
    first_stage_k: int = 10,
    final_k: int = 6,
) -> str:
    """
    Search the Manim documentation (modules, classes, functions, methods, examples).
    """
    base_retriever = vector_store.as_retriever(
        search_kwargs={"k": first_stage_k}
    )

    docs = base_retriever.invoke(query)
    # docs = rerank_docs(query, docs, top_k=final_k)

    lines = []
    for i, d in enumerate(docs, start=1):
        m = d.metadata
        header = (
            f"[{i}] "
            f"{m.get('qualified_name') or m.get('symbol_name') or 'Unknown'} "
            f"({m.get('module', 'unknown module')})"
        )
        snippet = d.page_content.replace("\n", " ")
        lines.append(header)
        lines.append(snippet)
        lines.append("---")

    return "\n".join(lines)


__all__ = ["mcp"]