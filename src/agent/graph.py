"""LangGraph agent with MCP tools.

Uses lazy async initialization for MCP tools with background pre-warming.
MCP servers run in separate processes with redirected output to log files.
"""

from __future__ import annotations

import os
import sys
import asyncio
import threading
from pathlib import Path
from typing import Annotated

# # LangChain
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage

# # LangChain MCP  
from langchain_mcp_adapters.client import MultiServerMCPClient

# # LangGraph
from langgraph.graph import StateGraph, END, MessagesState
from langgraph.prebuilt import ToolNode

# # .py Files
from agent.prompts import (
    MANIM_AGENT_PROMPT,
)

from dotenv import load_dotenv

load_dotenv()


# # Pre-requisties and variables

QWEN = "qwen/qwen3-vl-235b-a22b-instruct"
OPENAI = "gpt-4.1-mini"

TAVILY_API_KEY = os.environ.get('TAVILY_API_KEY')

# Get the absolute path to mcp_server.py and logs directory
MCP_SERVER_PATH = str(Path(__file__).parent / "mcp_server.py")
LOGS_DIR = Path(__file__).parent.parent.parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)


# # # Qwen LLM
# llm = ChatOpenAI(
#     api_key=os.environ.get("OPENROUTER_API_KEY", "n/a"),
#     base_url="https://openrouter.ai/api/v1",
#     model=QWEN,
#     temperature=0.1,
# )

# OpenAI LLM
llm = ChatOpenAI(
    model=OPENAI,
    temperature=0.1,
)

# MCP Configuration
MCP_CONFIG = {
    "manim_docs": {
        "transport": "stdio",
        "command": "python",
        "args": [MCP_SERVER_PATH],
        "env": os.environ.copy(),
    },
    "wikipedia": {
        "transport": "stdio",
        "command": "wikipedia-mcp",
        "args": ["--transport", "stdio"],
    },
    "tavily": {
        "transport": "streamable_http",
        "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={TAVILY_API_KEY}"
    }
}


# Cached tools and initialization state
_tools_cache = None
_client_cache = None
_initialization_lock = threading.Lock()
_initialization_started = False


async def get_mcp_tools():
    """Get or initialize MCP tools (lazy async initialization)."""
    global _tools_cache, _client_cache
    
    if _tools_cache is None:
        if _client_cache is None:
            print("🔧 Initializing MCP clients...", file=sys.stderr)
            _client_cache = MultiServerMCPClient(MCP_CONFIG)
        
        print("🔌 Connecting to MCP servers...", file=sys.stderr)
        _tools_cache = await _client_cache.get_tools()
        print(f"✅ Loaded {len(_tools_cache)} tools from MCP servers", file=sys.stderr)
    
    return _tools_cache


def pre_warm_mcp_in_background():
    """Pre-initialize MCP connections in a background thread."""
    global _initialization_started
    
    with _initialization_lock:
        if _initialization_started:
            return
        _initialization_started = True
    
    def _background_init():
        """Background thread function to warm up MCP connections."""
        try:
            print("🚀 Pre-warming MCP connections in background...", file=sys.stderr)
            # Run the async initialization in this thread
            asyncio.run(get_mcp_tools())
            print("✨ MCP connections ready!", file=sys.stderr)
        except Exception as e:
            print(f"⚠️  MCP pre-warm failed (will retry on first use): {e}", file=sys.stderr)
    
    # Start the background thread
    thread = threading.Thread(target=_background_init, daemon=True, name="MCPPreWarmer")
    thread.start()


# Agent node - calls LLM with tools
async def call_agent(state: MessagesState):
    """Call the agent with tools."""
    tools = await get_mcp_tools()
    llm_with_tools = llm.bind_tools(tools)
    
    # Add system message with prompt if not already there
    messages = state["messages"]
    if not messages or not any(m.type == "system" for m in messages):
        from langchain_core.messages import SystemMessage
        messages = [SystemMessage(content=MANIM_AGENT_PROMPT)] + messages
    
    response = await llm_with_tools.ainvoke(messages)
    return {"messages": [response]}


# Tool execution node
async def call_tools(state: MessagesState):
    """Execute tool calls."""
    tools = await get_mcp_tools()
    tool_node = ToolNode(tools)
    return await tool_node.ainvoke(state)


# Routing logic
def should_continue(state: MessagesState):
    """Route to tools or end."""
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return END


# Build the graph (synchronous function)
def build_graph():
    """Build the react agent graph."""
    workflow = StateGraph(MessagesState)
    
    workflow.add_node("agent", call_agent)
    workflow.add_node("tools", call_tools)
    
    workflow.set_entry_point("agent")
    workflow.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
    workflow.add_edge("tools", "agent")
    
    return workflow.compile()


# Pre-warm MCP connections in background when module loads
# This makes the first request faster and separates init logs from request logs
pre_warm_mcp_in_background()

# Export - no async at module level!
graph = build_graph()


