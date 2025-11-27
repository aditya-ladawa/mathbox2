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
from langchain_core.tools import InjectedToolCallId, tool
from langgraph.prebuilt import InjectedState
from langgraph.types import Command
from langgraph.prebuilt.chat_agent_executor import AgentState


# # LangChain MCP  
from langchain_mcp_adapters.client import MultiServerMCPClient


# # LangGraph
from langgraph.prebuilt import ToolNode
from langchain.agents import create_agent


# Import from other py files
from agent.task_tool import _create_task_tool
from agent.prompts import (
    MAIN_AGENT_PROMPT,
    RESEARCHER_PROMPT,
    CODER_PROMPT,
    DEBUGGER_PROMPT,
    get_today_str
)
from langgraph.prebuilt import create_react_agent


from dotenv import load_dotenv

load_dotenv()



# # LLMs

# # Main LLM (for all agents)
llm = ChatOpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY", "n/a"),
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    temperature=0.0,
)


# llm = ChatOpenAI(
#     api_key=os.environ.get("OPENROUTER_API_KEY", "n/a"),
#     base_url="https://openrouter.ai/api/v1",
#     model="qwen/qwen3-next-80b-a3b-instruct",
#     temperature=0.1,
# )

# # DeepSeek Reasoner for Think Tool

# Note: DeepSeek removed reasoner model, using regular chat for now
reasoner_llm = ChatOpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY", "n/a"),
    base_url="https://api.deepseek.com",
    model="deepseek-chat",  # Using chat model instead of reasoner
    temperature=0.1,
)


# reasoner_llm = ChatOpenAI(
#     api_key=os.environ.get("OPENROUTER_API_KEY", "n/a"),
#     base_url="https://openrouter.ai/api/v1",
#     model="qwen/qwen3-next-80b-a3b-instruct",
#     temperature=0.1,
# )


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
    """Agent state with scratchpad (todos) for complex workflow tracking."""
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



@tool(parse_docstring=True)
def think_strategically(reflection: str) -> str:
    """Strategic planning and reflection tool using advanced reasoning.
    
    Use this for complex decision-making, planning, and reflection.
    This is powered by a reasoning model that can think deeply about problems.
    
    When to use:
    - After research: Plan animation structure
    - Before coding: Design scene sequence
    - When debugging: Analyze error patterns
    - At decision points: Choose best approach
    
    Reflection should address:
    1. Current situation - What have I learned/accomplished?
    2. Analysis - What does this mean for the task?
    3. Options - What are the possible next steps?
    4. Decision - What's the best path forward?
    
    Args:
        reflection: Your detailed reflection on current status and planning
    """
    try:
        response = reasoner_llm.invoke([
            SystemMessage(content="You are a strategic planning assistant. Analyze the situation and provide clear, actionable guidance. Be logical, concise, and talk in cold and sharp manner."),
            HumanMessage(content=f"Reflect on this situation and provide strategic guidance:\n\n{reflection}")
        ])
        return f"💭 Strategic Analysis:\n\n{response.content}"
    except Exception as e:
        # Fallback if DeepSeek fails
        return f"✅ Reflection recorded:\n{reflection}\n\n(Note: Advanced reasoning unavailable: {e})"


# # Tool Loading Helper (Lazy)

_mcp_tools_cache = None
_mcp_tools_lock = threading.Lock()

def get_all_tools():
    """Get all MCP tools (cached, lazy-loaded).
    
    Tools are ONLY loaded when this function is called (during agent first use),
    not during module import. This prevents blocking langgraph dev.
    """
    global _mcp_tools_cache
    
    if _mcp_tools_cache is not None:
        return _mcp_tools_cache
    
    with _mcp_tools_lock:
        if _mcp_tools_cache is not None:
            return _mcp_tools_cache
            
        # Load tools synchronously (only on first actual use)
        _mcp_tools_cache = asyncio.run(get_mcp_tools())
        return _mcp_tools_cache


# # Deep Agent Construction



# Load all MCP tools
print("📦 Loading MCP tools...")
mcp_tools = get_all_tools()
print(f"✅ Loaded {len(mcp_tools)} MCP tools")

# State management tools
state_tools = [read_todos, write_todos, think_strategically]

# All tools available to sub-agents
all_tools = mcp_tools + state_tools

# Sub-Agent Configurations
sub_agents = [
    {
        "name": "researcher",
        "description": "Research Manim APIs and mathematical concepts. Returns FULL documentation (no summarization).",
        "prompt": RESEARCHER_PROMPT.format(date=get_today_str()),
        "tools": ["manim_docs_search", "search_wikipedia", "tavily_search", "think_strategically"]
    },
    {
        "name": "coder",
        "description": "Write clean, beautiful Manim animation code following style guide.",
        "prompt": CODER_PROMPT,
        "tools": ["write_file", "edit_file", "read_file", "list_files", "manim_docs_search", "find_files", "think_strategically"]
    },
    {
        "name": "debugger",
        "description": "Execute Manim renders, diagnose errors, and fix code systematically.",
        "prompt": DEBUGGER_PROMPT,
        "tools": ["execute_command", "read_file", "edit_file", "manim_docs_search", "tavily_search", "find_files", "think_strategically"]
    }
]

print(f"🤖 Configuring {len(sub_agents)} sub-agents...")

# Create task delegation tool
task_tool = _create_task_tool(
    tools=all_tools,
    subagents=sub_agents,
    model=llm,
    state_schema=DeepAgentState
)

print("✅ Task delegation tool created")

# Main agent tools (delegation + state management)
main_agent_tools = [task_tool, read_todos, write_todos, think_strategically]


from langgraph.checkpoint.memory import MemorySaver


checkpointer = MemorySaver()

# Create the main deep agent
print("🧠 Building main deep agent...")
deep_graph = create_react_agent(
    llm,
    tools=main_agent_tools,
    prompt=MAIN_AGENT_PROMPT.format(date=get_today_str()),
    state_schema=DeepAgentState,
    # checkpointer=checkpointer,
)

print("✅ Deep agent ready!")
print()
print("Available sub-agents:")
for agent in sub_agents:
    print(f"  - {agent['name']}: {agent['description']}")
print()

__all__ = ["deep_graph", "DeepAgentState"]


# # Test Main Function

async def main():
    """Test the deep agent with a simple query."""
    inputs = {
        "messages": [
            ("user", "Please teach me newton's method of descent")
        ]
    }
    
    config = {"configurable": {"thread_id": "thread-1"}, "recursion_limit": 1000}
    
    print("\n" + "="*50)
    print("🧪 Testing Deep Agent")
    print("="*50 + "\n")
    
    async for event in deep_graph.astream(inputs, config=config, stream_mode="values"):
        event["messages"][-1].pretty_print()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
