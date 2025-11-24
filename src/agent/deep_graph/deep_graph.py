from __future__ import annotations

import os
import sys
import asyncio
import threading
import re
import subprocess
from pathlib import Path
from datetime import datetime

# # Type hints
from typing_extensions import Annotated, NotRequired, TypedDict, Literal

# # LangChain
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, ToolMessage, HumanMessage, SystemMessage
from langgraph.prebuilt.chat_agent_executor import AgentState
from langchain_core.tools import InjectedToolCallId, tool
from langgraph.prebuilt import InjectedState
from langgraph.types import Command


# # LangChain MCP  
from langchain_mcp_adapters.client import MultiServerMCPClient


# # LangGraph
from langgraph.prebuilt import ToolNode
from langchain.agents import create_agent

from dotenv import load_dotenv

load_dotenv()


# # Workspace Configuration
WORKSPACE_ROOT = Path(__file__).parent.parent.parent.parent / "manim_workspace"
WORKSPACE_ROOT.mkdir(parents=True, exist_ok=True)  # Create if doesn't exist

# Create subdirectories
(WORKSPACE_ROOT / "scenes").mkdir(exist_ok=True)
(WORKSPACE_ROOT / "assets").mkdir(exist_ok=True)


# # MCP Client Configuration
async def get_mcp_tools():
    """Load MCP tools from all configured servers.
    
    Available MCP servers:
    - manim_filesystem: File operations (list, read, write, edit, search, find, execute)
    - manim_docs: Qdrant vector search for Manim documentation
    - wikipedia: Wikipedia article search and retrieval
    - tavily: Web search for tutorials, Stack Overflow, etc.
    """
    # Get environment variables
    tavily_api_key = os.environ.get("TAVILY_API_KEY")
    
    # Build MCP configuration
    mcp_config = {
        # Filesystem tools
        "manim_filesystem": {
            "transport": "stdio",
            "command": "python",
            "args": [str(Path(__file__).parent / "file_mcp_server.py")],
            "env": os.environ.copy(),
        },
        # Manim documentation search (Qdrant)
        "manim_docs": {
            "transport": "stdio",
            "command": "python",
            "args": [str(Path(__file__).parent / "research_mcp_server.py")],
            "env": os.environ.copy(),
        },
    }
    
    # Add Wikipedia if available
    try:
        mcp_config["wikipedia"] = {
            "transport": "stdio",
            "command": "wikipedia-mcp",
            "args": ["--transport", "stdio"],
        }
    except Exception:
        print("⚠️  Wikipedia MCP not available", file=sys.stderr)
    
    # Add Tavily if API key is available
    if tavily_api_key:
        mcp_config["tavily"] = {
            "transport": "streamable_http",
            "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={tavily_api_key}"
        }
    else:
        print("⚠️  TAVILY_API_KEY not set - Tavily search unavailable", file=sys.stderr)
    
    client = MultiServerMCPClient(mcp_config)
    return await client.get_tools()


# # Security Helpers

def _ensure_safe_path(path: str) -> Path:
    """Ensure path is within workspace and return absolute Path.
    
    Args:
        path: File path (should start with / for virtual paths)
        
    Returns:
        Absolute Path object within workspace
        
    Raises:
        ValueError: If path is outside workspace or contains traversal
    """
    # Treat as virtual path under workspace
    vpath = path if path.startswith("/") else "/" + path
    
    # Block path traversal
    if ".." in vpath or vpath.startswith("~"):
        raise ValueError("Path traversal not allowed")
    
    # Resolve to absolute path
    full_path = (WORKSPACE_ROOT / vpath.lstrip("/")).resolve()
    
    # Ensure it's within workspace
    try:
        full_path.relative_to(WORKSPACE_ROOT)
    except ValueError:
        raise ValueError(f"Access denied: {path} is outside workspace") from None
    
    return full_path


def _format_with_line_numbers(content: str, start_line: int = 1) -> str:
    """Format content with line numbers (cat -n style).
    
    Args:
        content: File content as string
        start_line: Starting line number
        
    Returns:
        Formatted content with line numbers
    """
    lines = content.splitlines()
    result = []
    for i, line in enumerate(lines, start=start_line):
        result.append(f"{i:6d}\t{line}")
    return "\n".join(result)


# # State and schemas

class Todo(TypedDict):
    """A structured task item for tracking progress through complex workflows.

    Attributes:
        content: Short, specific description of the task
        status: Current state - pending, in_progress, or completed
    """

    content: str
    status: Literal["pending", "in_progress", "completed"]
    


class DeepAgentState(AgentState):
    """
    Extend ReAct agent state with scratchpad and ACTUAL FileSystemBackend.
    """
    todos: NotRequired[list[Todo]]
    

# # todo tools

@tool(parse_docstring=True)
def read_todos(
    state: Annotated[DeepAgentState, InjectedState],
    tool_call_id: Annotated[str, InjectedToolCallId],
) -> str:
    """Read the current todo list from the agent state.

    This tool allows the agent to retrieve and review the current todo list
    to stay focused on remaining tasks and track progress through complex workflows.

    Args:
        state: Injected agent state containing the current todo list
        tool_call_id: Injected tool call identifier for message tracking

    Returns:
        Formatted string representation of the current todo list
    """
    todos = state.get("todos", [])
    if not todos:
        return "No todos currently in the list."

    result = "Current TODO List:\n"
    for i, todo in enumerate(todos, 1):
        status_emoji = {"pending": "⏳", "in_progress": "🔄", "completed": "✅"}
        emoji = status_emoji.get(todo["status"], "❓")
        result += f"{i}. {emoji} {todo['content']} ({todo['status']})\n"

    return result.strip()


@tool(parse_docstring=True)
def write_todos(
    todos: list[Todo], 
    tool_call_id: Annotated[str, InjectedToolCallId]
) -> Command:
    """Create or update the agent's todo list for task planning and tracking.

    Args:
        todos: List of todo items with content and status
        tool_call_id: Tool call identifier for message response

    Returns:
        Command to update agent state with new todo list
    """
    return Command(
        update={
            "todos": todos,
            "messages": [
                ToolMessage(f"Updated todo list to {todos}", tool_call_id=tool_call_id)
            ],
        }
    )

