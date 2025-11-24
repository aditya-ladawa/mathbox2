"""Research MCP Server for Manim Documentation.

This module provides search capabilities for Manim documentation using
Qdrant vector store with hybrid search (dense + sparse embeddings) and
optional reranking with Voyage AI for improved result quality.
"""

import os
import requests
from typing import List, Literal
from pathlib import Path

from dotenv import load_dotenv
from fastmcp import FastMCP
from langchain_qdrant import QdrantVectorStore, FastEmbedSparse, RetrievalMode
from langchain_core.documents import Document

# Load environment variables
load_dotenv()

# Import embeddings
import sys
sys.path.insert(0, str(Path(__file__).parent))
from embeddings import OpenRouterQwen3Embeddings

# FastMCP server
mcp = FastMCP("ManimResearch")

# Environment variables
QDRANT_URL = os.environ.get("QDRANT_URL")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")
VOYAGE_API_KEY = os.environ.get("VOYAGEAI_API_KEY")
COLLECTION_NAME = os.environ.get("MANIM_COLLECTION_NAME", "manim_docs_qwen3_embed")

if not QDRANT_URL:
    raise RuntimeError("QDRANT_URL is not set in environment")
if not QDRANT_API_KEY:
    raise RuntimeError("QDRANT_API_KEY is not set in environment")

# Initialize embeddings
dense_embeddings = OpenRouterQwen3Embeddings()
sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")

# Initialize vector store
try:
    vector_store = QdrantVectorStore.from_existing_collection(
        collection_name=COLLECTION_NAME,
        embedding=dense_embeddings,
        sparse_embedding=sparse_embeddings,
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        prefer_grpc=False,
        retrieval_mode=RetrievalMode.HYBRID,
    )
except Exception as e:
    print(f"Warning: Could not connect to Qdrant: {e}")
    vector_store = None


def rerank_docs(query: str, docs: List[Document], top_k: int = 6) -> List[Document]:
    """Rerank documents using Voyage AI for improved relevance.
    
    Args:
        query: Search query
        docs: List of documents to rerank
        top_k: Number of top results to return
        
    Returns:
        Reranked list of documents
    """
    if not docs or not VOYAGE_API_KEY:
        return docs[:top_k]

    try:
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
        
    except Exception as e:
        print(f"Warning: Reranking failed, using original order: {e}")
        return docs[:top_k]


@mcp.tool()
def manim_docs_search(
    query: str,
    k: int = 6,
    first_stage_k: int = 10,
    use_reranking: bool = False,
    filter_type: Literal["all", "class", "function", "method", "example"] | None = None,
) -> str:
    """Search Manim documentation with hybrid vector search and optional reranking.
    
    Returns COMPLETE documentation (no summarization) for technical accuracy.
    Use this to find:
    - API documentation (classes, methods, parameters)
    - Mathematical formulas and equations
    - Working code examples
    - Complete docstrings
    
    Args:
        query: Search query (e.g., "Circle class", "create animation", "Fourier series")
        k: Number of final results to return (default: 6)
        first_stage_k: Number of results to retrieve before reranking (default: 10)
        use_reranking: Whether to use Voyage AI reranking (default: True if API key available)
        filter_type: Filter by documentation type (default: "all")
        
    Returns:
        Complete documentation with:
        - Qualified name (module.Class.method)
        - Full docstring
        - Parameters and return types  
        - Code examples
        - Related symbols
        
    Example:
        result = manim_docs_search("Circle animation", k=3)
        # Returns full API docs for Circle class with all methods,
        # reranked by relevance to "Circle animation"
    """
    if not vector_store:
        return "Error: Manim docs search unavailable (Qdrant not connected)"
    
    try:
        # Create retriever with first-stage k
        retriever = vector_store.as_retriever(
            search_kwargs={"k": first_stage_k}
        )
        
        # Perform search
        docs = retriever.invoke(query)
        
        if not docs:
            return f"No results found for '{query}'. Try a different query."
        
        # Rerank if enabled and API key available
        if use_reranking and VOYAGE_API_KEY:
            docs = rerank_docs(query, docs, top_k=k)
        else:
            docs = docs[:k]
        
        # Format results with FULL content (no summarization)
        lines = []
        rerank_note = " (reranked by relevance)" if use_reranking and VOYAGE_API_KEY else ""
        lines.append(f"🔍 Found {len(docs)} result(s) for '{query}'{rerank_note}:\n")
        
        for i, doc in enumerate(docs, start=1):
            m = doc.metadata
            
            # Header with qualified name and module
            qualified_name = m.get('qualified_name') or m.get('symbol_name', 'Unknown')
            module = m.get('module', 'unknown module')
            doc_type = m.get('type', 'unknown')
            
            lines.append(f"[{i}] {qualified_name}")
            lines.append(f"    Module: {module}")
            lines.append(f"    Type: {doc_type}")
            
            # Full content (critical for technical accuracy)
            content = doc.page_content
            if content:
                lines.append(f"\n{content}\n")
            
            lines.append("─" * 70)
        
        result = "\n".join(lines)
        
        # Add usage hint
        result += f"\n\n💡 Tip: Found {len(docs)} results. Read full details above for exact API usage."
        
        return result
        
    except Exception as e:
        return f"Error searching Manim docs: {e}"


@mcp.tool()
def think_about_manim(reflection: str) -> str:
    """Strategic reflection tool for planning Manim animations.
    
    Use this to think through complex animation workflows before coding.
    
    When to use:
    - After searching docs: What APIs did I find? Do I understand them?
    - Before writing code: What's the logical sequence of animations?
    - When debugging: What could be causing this error?
    - Planning complexity: Do I need multiple scenes or one complex scene?
    
    Reflection should address:
    1. **Understanding**: Do I have complete API knowledge needed?
    2. **Planning**: What's the sequence of Manim objects and animations?
    3. **Gaps**: What specific technical details am I missing?
    4. **Decision**: Am I ready to write code or need more research?
    
    Args:
        reflection: Your detailed thoughts on the animation plan
        
    Returns:
        Confirmation that reflection was recorded

    """
    return f"✅ Reflection recorded:\n{reflection}"


# Run MCP server if executed directly
if __name__ == "__main__":
    mcp.run()
