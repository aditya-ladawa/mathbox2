# # Graph DB indexing, but takes insane time, so we didn't proceed with this approach.

import os
import re
import asyncio
from pathlib import Path
from dotenv import load_dotenv

from lightrag import LightRAG, QueryParam
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import EmbeddingFunc
from lightrag.llm.openai import openai_complete_if_cache, openai_embed

load_dotenv()

# ============================================================
# Config
# ============================================================
WORKING_DIR = os.getenv("WORKING_DIR", "./manim_lightrag")

# We have a single markdown file: unified_manim_community_docs.md
# You can override via MD_FILE env if needed.
MD_FILE = os.getenv("MD_FILE", "./unified_manim_community_docs.md")

# Qwen3 embedding model on OpenRouter typically has 1536 dims.
# If it differs, just set EMBEDDING_DIM in your .env accordingly.
EMBED_DIM = int(os.getenv("EMBEDDING_DIM", "4096"))

# You said your embedding model supports ~32k tokens.
MAX_EMBED_TOKENS = int(os.getenv("MAX_EMBED_TOKENS", "32000"))

# Just one file, but keep this for future expansion
FILE_PARALLEL = int(os.getenv("MAX_PARALLEL_INSERT", "4"))

# ============================================================
# LLM via OpenRouter (Qwen3)
# ============================================================
async def llm_model_func(
    prompt: str,
    system_prompt: str | None = None,
    history_messages: list[dict] | None = None,
    **kwargs,
) -> str:
    """
    Qwen3 LLM through OpenRouter, using LightRAG's OpenAI-compatible helper.
    """
    return await openai_complete_if_cache(
        # Default to Qwen3 VL 30B on OpenRouter; override via LLM_MODEL if you want
        os.getenv("LLM_MODEL", "qwen/qwen3-vl-30b-a3b-instruct"),
        prompt,
        system_prompt=system_prompt,
        history_messages=history_messages or [],
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url=os.getenv("LLM_BINDING_HOST", "https://openrouter.ai/api/v1"),
        **kwargs,
    )


# ============================================================
# Embeddings via OpenRouter (Qwen3 embedding)
# ============================================================
def _embed(texts: list[str]) -> list[list[float]]:
    """
    Qwen3 embedding through OpenRouter, using LightRAG's openai_embed helper.
    LightRAG will manage batching / async using env vars like:
      - EMBEDDING_FUNC_MAX_ASYNC
      - EMBEDDING_BATCH_NUM
    """
    return openai_embed(
        texts,
        model=os.getenv("EMBEDDING_MODEL", "qwen/qwen3-embedding-8b"),
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url=os.getenv("EMBEDDING_BINDING_HOST", "https://openrouter.ai/api/v1"),
    )


embedding_func = EmbeddingFunc(
    embedding_dim=EMBED_DIM,
    max_token_size=MAX_EMBED_TOKENS,
    func=_embed,
)

# ============================================================
# Helpers
# ============================================================
IMG_MD = re.compile(r"!\[[^\]]*\]\([^)]+\)")  # strip image links; text-only ingest


def load_markdown_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    return IMG_MD.sub("", text)


async def ingest_markdown_file(rag: LightRAG, md_path: Path):
    """
    Ingest a single markdown file (your unified Manim docs).
    """
    if not md_path.is_file():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    content = load_markdown_text(md_path)
    if not content.strip():
        print(f"{md_path} is empty; skipping.")
        return

    sem = asyncio.Semaphore(max(1, FILE_PARALLEL))

    async with sem:
        # file_paths is just metadata stored by LightRAG
        await rag.ainsert(content, file_paths=str(md_path))
        print(f"📄 Ingested {md_path.name}")

    print("✅ Finished ingestion of unified markdown file.")


# ============================================================
# Build the DB (graph + vector index)
# ============================================================
async def build_db(md_file: str):
    os.makedirs(WORKING_DIR, exist_ok=True)

    rag = LightRAG(
        working_dir=WORKING_DIR,
        llm_model_func=llm_model_func,
        embedding_func=embedding_func,
        # NOTE: reranker will be enabled via QueryParam + env config (see below)
    )

    await rag.initialize_storages()
    await initialize_pipeline_status()

    try:
        print(
            "Concurrency -> docs:", FILE_PARALLEL,
            "| LLM MAX_ASYNC:", os.getenv("MAX_ASYNC", "default"),
            "| EMBEDDING_FUNC_MAX_ASYNC:", os.getenv("EMBEDDING_FUNC_MAX_ASYNC", "default"),
            "| EMBEDDING_BATCH_NUM:", os.getenv("EMBEDDING_BATCH_NUM", "default"),
        )

        await ingest_markdown_file(rag, Path(md_file))
    finally:
        await rag.finalize_storages()


# ============================================================
# Query the DB
# ============================================================
async def query_db(questions: list[str]):
    rag = LightRAG(
        working_dir=WORKING_DIR,
        llm_model_func=llm_model_func,
        embedding_func=embedding_func,
    )

    await rag.initialize_storages()
    await initialize_pipeline_status()

    try:
        for q in questions:
            print(f"\nQ: {q}")
            ans = await rag.aquery(
                q,
                param=QueryParam(
                    mode="mix",          # both graph + vector
                    top_k=8,
                    stream=False,
                    enable_rerank=True,  # <--- let LightRAG use the reranker
                ),
            )
            print(ans)
    finally:
        await rag.finalize_storages()


# ============================================================
# Entry point
# ============================================================
if __name__ == "__main__":
    mode = os.getenv("MODE", "ingest")  # MODE=ingest or MODE=query
    md_file = MD_FILE

    if mode == "ingest":
        asyncio.run(build_db(md_file))
    else:
        questions = [
            "How can I draw and animate a star shape in Manim?",
            "How do I configure scenes and global settings in Manim?",
        ]
        asyncio.run(query_db(questions))


# # lightrag-server --working-dir ./manim_lightrag --input-dir ./uploads --port 9621