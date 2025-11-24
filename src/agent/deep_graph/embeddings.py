"""OpenRouter Qwen3 Embeddings for Manim Documentation.

This module provides LangChain-compatible embeddings using OpenRouter's
qwen/qwen3-embedding-8b model for efficient, accurate vector search.
"""

import os
from typing import List, Optional, Dict

from openai import OpenAI
from langchain_core.embeddings import Embeddings


class OpenRouterQwen3Embeddings(Embeddings):
    """LangChain Embeddings wrapper for OpenRouter qwen/qwen3-embedding-8b.

    Uses OPENROUTER_API_KEY from environment variables.
    
    Attributes:
        model: Model identifier (default: "qwen/qwen3-embedding-8b")
        api_key: OpenRouter API key
        client: OpenAI client configured for OpenRouter
        extra_headers: Optional headers for routing and analytics
    """

    def __init__(
        self,
        model: str = "qwen/qwen3-embedding-8b",
        api_key: Optional[str] = None,
        site_url: Optional[str] = None,
        site_title: Optional[str] = None,
    ):
        """Initialize OpenRouter Qwen3 embeddings.
        
        Args:
            model: Model identifier (default: qwen/qwen3-embedding-8b)
            api_key: OpenRouter API key (defaults to OPENROUTER_API_KEY env var)
            site_url: Optional site URL for OpenRouter analytics
            site_title: Optional site title for OpenRouter analytics
            
        Raises:
            ValueError: If API key is not provided or not in environment
        """
        self.model = model
        self.api_key = api_key or os.environ.get("OPENROUTER_API_KEY")
        
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY is not set in environment")

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.api_key,
        )

        # Optional headers recommended by OpenRouter
        self.extra_headers: Dict[str, str] = {}
        if site_url:
            self.extra_headers["HTTP-Referer"] = site_url
        if site_title:
            self.extra_headers["X-Title"] = site_title

    def _embed(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts.
        
        Args:
            texts: List of strings to embed
            
        Returns:
            List of embedding vectors
            
        Raises:
            RuntimeError: If API call fails or returns no data
        """
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
        """Embed a list of documents.
        
        Args:
            texts: List of document texts to embed
            
        Returns:
            List of embedding vectors
        """
        return self._embed(texts)

    def embed_query(self, text: str) -> List[float]:
        """Embed a single query text.
        
        Args:
            text: Query text to embed
            
        Returns:
            Single embedding vector
        """
        return self._embed([text])[0]
