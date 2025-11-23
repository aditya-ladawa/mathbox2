"""Test agent using MCP filesystem tools.

This script demonstrates loading MCP tools and using them with a LangGraph agent.
"""

import os
import asyncio
from pathlib import Path

from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from langchain_core.messages import ToolMessage
from langchain_core.tools import InjectedToolCallId
from langgraph.prebuilt import InjectedState
from langgraph.types import Command
from typing_extensions import Annotated, TypedDict, Literal, NotRequired

# Import MCP tools
import sys
sys.path.insert(0, str(Path(__file__).parent))

from dotenv import load_dotenv
load_dotenv()

# LLM Configuration
DEEPSEEK = "deepseek-chat"

llm = ChatOpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY", "n/a"),
    base_url="https://api.deepseek.com",
    model=DEEPSEEK,
    temperature=0.1,
)


# # State and Todo Tools (from deep_graph.py)

class Todo(TypedDict):
    content: str
    status: Literal["pending", "in_progress", "completed"]


@tool
def read_todos(
    state: Annotated[dict, InjectedState],
    tool_call_id: Annotated[str, InjectedToolCallId],
) -> str:
    """Read the current todo list from the agent state."""
    todos = state.get("todos", [])
    if not todos:
        return "No todos currently in the list."

    result = "Current TODO List:\n"
    for i, todo in enumerate(todos, 1):
        status_emoji = {"pending": "⏳", "in_progress": "🔄", "completed": "✅"}
        emoji = status_emoji.get(todo["status"], "❓")
        result += f"{i}. {emoji} {todo['content']} ({todo['status']})\n"

    return result.strip()


@tool
def write_todos(
    todos: list[Todo], 
    tool_call_id: Annotated[str, InjectedToolCallId]
) -> Command:
    """Create or update the agent's todo list for task planning and tracking."""
    return Command(
        update={
            "todos": todos,
            "messages": [
                ToolMessage(f"Updated todo list to {todos}", tool_call_id=tool_call_id)
            ],
        }
    )


# System prompt for testing
SYSTEM_PROMPT = """You are a filesystem tool tester. Test the following tools systematically:

1. **write_file**: Create /test/hello.py with: print("Hello Manim!")
2. **list_files**: List files in /test/
3. **read_file**: Read /test/hello.py
4. **edit_file**: Change "Hello" to "Greetings" in /test/hello.py
5. **read_file**: Read again to verify edit
6. **find_files**: Find all *.py files in /test/
7. **search_files**: Search for "Greetings" in /test/

For each tool, report if it works correctly.
After testing, provide a summary.
"""


async def test_agent():
    """Test the agent with MCP tools."""
    
    print("=" * 70)
    print("MCP Tools Agent Test")
    print("=" * 70)
    print()
    
    # Load MCP tools using LangChain MCP adapter
    print("Loading MCP tools via LangChain MCP adapter...")
    from langchain_mcp_adapters.client import MultiServerMCPClient
    
    mcp_server_path = str(Path(__file__).parent / "mcp_server.py")
    
    mcp_config = {
        "manim_filesystem": {
            "transport": "stdio",
            "command": "python",
            "args": [mcp_server_path],
            "env": os.environ.copy(),
        }
    }
    
    client = MultiServerMCPClient(mcp_config)
    mcp_tools = await client.get_tools()
    
    print(f"✅ Loaded {len(mcp_tools)} MCP tools")
    for i, tool in enumerate(mcp_tools, 1):
        print(f"   {i}. {tool.name}")
    print()
    
    # Add todo tools
    all_tools = list(mcp_tools) + [read_todos, write_todos]
    print(f"✅ Total tools: {len(all_tools)}")
    print()
    
    # Create agent
    print("Creating agent...")
    agent = create_react_agent(
        llm,
        tools=all_tools
    )
    print("✅ Agent created")
    print()
    
    # Run agent
    print("-" * 70)
    print("Running agent test...")
    print("-" * 70)
    print()
    
    result = await agent.ainvoke({
        "messages": [
            ("system", SYSTEM_PROMPT),
            ("user", "Please test all the filesystem tools as described in your instructions.")
        ]
    })
    
    print()
    print("-" * 70)
    print("Agent Output:")
    print("-" * 70)
    print()
    
    # Print messages
    for msg in result["messages"]:
        if hasattr(msg, "content") and msg.content:
            print(f"[{msg.__class__.__name__}]:")
            print(msg.content)
            print()
    
    print("=" * 70)
    print("Test Complete")
    print("=" * 70)


if __name__ == "__main__":
    print("\n🚀 Starting MCP Tools Agent Test\n")
    asyncio.run(test_agent())
    print("\n✅ Done\n")
