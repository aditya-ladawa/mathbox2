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
    get_today_str
)
from langgraph.prebuilt import create_react_agent


from dotenv import load_dotenv

load_dotenv()



# # LLMs

# Main Orchestrator LLM (DeepSeek for strategic planning and delegation)
main_llm = ChatOpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY", "n/a"),
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    temperature=0.1,
)

# Researcher LLM (Qwen for research)
researcher_llm = ChatOpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY", "n/a"),
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    temperature=0.5,
)

# Coding LLM (Qwen3-Coder-Plus for Manim code generation)
coding_llm = ChatOpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY", "n/a"),
    base_url="https://openrouter.ai/api/v1",
    model="qwen/qwen3-coder-plus",
    temperature=0.0,
)

# Keep reference for backward compatibility
llm = main_llm

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

    scene_file: NotRequired[str]
    scene_class: NotRequired[str]
    research_notes_path: NotRequired[str]

    

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
    """Tool for strategic reflection on research progress and decision-making.

    Use this tool after each search to analyze results and plan next steps systematically.
    This creates a deliberate pause in the research workflow for quality decision-making.

    When to use:
    - After receiving search results: What key information did I find?
    - Before deciding next steps: Do I have enough to answer comprehensively?
    - When assessing research gaps: What specific information am I still missing?
    - Before concluding research: Can I provide a complete answer now?
    - How complex is the question: Have I reached the number of search limits?

    Reflection should address:
    1. Analysis of current findings - What concrete information have I gathered?
    2. Gap assessment - What crucial information is still missing?
    3. Quality evaluation - Do I have sufficient evidence/examples for a good answer?
    4. Strategic decision - Should I continue searching or provide my answer?

    Args:
        reflection: Your detailed reflection on research progress, findings, gaps, and next steps

    Returns:
        Confirmation that reflection was recorded for decision-making
    """
    return f"Reflection recorded: {reflection}"


# # State Management tools
@tool(parse_docstring=True)
def set_research_notes_path(
    path: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
) -> Command:
    """
    Store the path to the research notes file in the agent state.

    Use this after writing a notes file summarizing relevant Manim API usage,
    math concepts, or planning information.

    Args:
        path: Absolute or virtual path to the notes file (e.g. "/assets/notes/fourier_intro.md")
    """
    return Command(
        update={
            "research_notes_path": path,
            "messages": [
                ToolMessage(
                    f"Research notes path set to: {path}",
                    tool_call_id=tool_call_id,
                )
            ],
        }
    )

@tool(parse_docstring=True)
def set_scene_metadata(
    scene_file: str,
    scene_class: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
) -> Command:
    """
    Store the main Manim scene file and class name for the current project.

    Use this right after creating or identifying the scene file and class.

    Args:
        scene_file: Full path to the scene Python file (e.g. "/scenes/complex_plane.py")
        scene_class: Name of the scene class inside that file (e.g. "ComplexPlaneIntro")
    """
    return Command(
        update={
            "scene_file": scene_file,
            "scene_class": scene_class,
            "messages": [
                ToolMessage(
                    f"Scene metadata updated: file={scene_file}, class={scene_class}",
                    tool_call_id=tool_call_id,
                )
            ],
        }
    )
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
state_tools = [read_todos, write_todos, think_strategically, set_research_notes_path, set_scene_metadata]

# All tools available to sub-agents
all_tools = mcp_tools + state_tools

# Sub-Agent Configurations (researcher + coder)
sub_agents = [
    {
        "name": "researcher",
        "description": "Research Manim APIs and mathematical concepts. Returns FULL documentation (no summarization).",
        "prompt": RESEARCHER_PROMPT.format(date=get_today_str()),
        "tools": ["manim_docs_search", "search_wikipedia", "tavily_search", "write_file", "read_file", "edit_file", "set_research_notes_path"]
    },
    {
        "name": "coder",
        "description": "Write, test, and debug Manim animation code. Executes renders and manages workspace files.",
        "prompt": CODER_PROMPT.format(date=get_today_str()),
        "tools": ["list_files", "read_file", "write_file", "edit_file", "search_files", "find_files", "manim_docs_search", "execute_command", "set_scene_metadata"]
    }
]

print(f"🤖 Configuring {len(sub_agents)} sub-agents...")

# Create task delegation tool with separate models for each agent type
task_tool = _create_task_tool(
    tools=all_tools,
    subagents=sub_agents,
    model=main_llm,  # Main orchestrator model (DeepSeek)
    researcher_model=researcher_llm,  # Researcher model (DeepSeek)
    coding_model=coding_llm,  # Coding model (Qwen3-Coder-Plus)
    state_schema=DeepAgentState
)

print("✅ Task delegation tool created")

# Get specific tools by name for main agent
tools_by_name = {tool.name: tool for tool in mcp_tools}

# Main agent tools (orchestration only: delegation and state management)
main_agent_tools = [
    # Delegation and state management only
    task_tool, 
    read_todos, 
    write_todos, 
    think_strategically,
]


from langgraph.checkpoint.memory import MemorySaver


checkpointer = MemorySaver()

# Create the main deep agent
print("🧠 Building main deep agent...")
deep_graph = create_react_agent(
    main_llm,  # Use DeepSeek for main orchestrator agent
    tools=main_agent_tools,
    prompt=MAIN_AGENT_PROMPT.format(date=get_today_str()),
    state_schema=DeepAgentState,
    # checkpointer=checkpointer,
)

print("✅ Deep agent ready!")
print()
print("Architecture: Deep Agent (3-agent system)")
print(f"  Main Orchestrator: Has {len(main_agent_tools)} tools (delegation and planning only)")
print(f"    Model: deepseek-chat")
print("  Sub-agents:")
for agent in sub_agents:
    if agent['name'] == "researcher":
        model_name = "deepseek-chat"
    elif agent['name'] == "coder":
        model_name = "qwen/qwen3-coder-plus"
    else:
        model_name = "deepseek-chat"
    print(f"    - {agent['name']}: {agent['description']}")
    print(f"      Model: {model_name}")
print()

__all__ = ["deep_graph", "DeepAgentState"]


# # Test Main Function

async def main():
    """Test the deep agent with a simple query."""
    inputs = {
        "messages": [
            ("user", "Can you explain me in detail on how Attention mechanism in transformer model.")
        ]
    }
    
    config = {"configurable": {"thread_id": "thread-3"}, "recursion_limit": 1000}
    
    print("\n" + "="*50)
    print("🧪 Testing Deep Agent")
    print("="*50 + "\n")
    
    async for event in deep_graph.astream(inputs, config=config, stream_mode="values"):
        event["messages"][-1].pretty_print()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
