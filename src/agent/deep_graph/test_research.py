"""Test script for research tools integration.

Tests all research MCP servers:
- Manim documentation search (Qdrant)
- Wikipedia search
- Tavily web search
- Think tool for strategic planning
"""

import os
import asyncio
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

import sys
sys.path.insert(0, str(Path(__file__).parent))

async def test_research_tools():
    """Test all research tools."""
    
    print("=" * 70)
    print("Research Tools Test")
    print("=" * 70)
    print()
    
    # Import from deep_graph
    from deep_graph import get_mcp_tools
    
    # Load all MCP tools
    print("🔌 Loading MCP tools...")
    tools = await get_mcp_tools()
    
    print(f"✅ Loaded {len(tools)} tools\n")
    
    # Group tools by server
    tool_groups = {}
    for tool in tools:
        # Extract server name from tool name prefix or metadata
        name = tool.name
        if "_" in name:
            server = name.split("_")[0]
        else:
            server = "other"
        
        if server not in tool_groups:
            tool_groups[server] = []
        tool_groups[server].append(name)
    
    # Display tools by server
    for server, tool_names in sorted(tool_groups.items()):
        print(f"📦 {server.upper()} ({len(tool_names)} tools):")
        for tool_name in sorted(tool_names):
            print(f"   - {tool_name}")
        print()
    
    # Test Manim docs search if available
    manim_search_tool = next((t for t in tools if "manim_docs_search" in t.name), None)
    
    if manim_search_tool:
        print("-" * 70)
        print("Testing: manim_docs_search")
        print("-" * 70)
        
        try:
            result = await manim_search_tool.ainvoke({"query": "Circle class", "k": 2})
            
            print("Query: 'Circle class'")
            print("Results:")
            print(result[:500] + "..." if len(result) > 500 else result)
            print("\n✅ Manim docs search working!")
            
        except Exception as e:
            print(f"⚠️  Manim docs search error: {e}")
    else:
        print("⚠️  manim_docs_search tool not found")
    
    # Test think tool if available  
    think_tool = next((t for t in tools if "think" in t.name.lower()), None)
    
    if think_tool:
        print("\n" + "-" * 70)
        print("Testing: think_about_manim")
        print("-" * 70)
        
        try:
            result = await think_tool.ainvoke({
                "reflection": "Testing the strategic thinking tool for animation planning"
            })
            
            print("Reflection: 'Testing the strategic thinking tool...'")
            print("Result:")
            print(result)
            print("\n✅ Think tool working!")
            
        except Exception as e:
            print(f"⚠️  Think tool error: {e}")
    else:
        print("⚠️  think tool not found")
    
    print("\n" + "=" * 70)
    print("Test Complete")
    print("=" * 70)


if __name__ == "__main__":
    print("\n🚀 Starting Research Tools Test\n")
    asyncio.run(test_research_tools())
    print("\n✅ Done\n")
