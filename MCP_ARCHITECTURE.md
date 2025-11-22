# MCP Server Architecture

## Overview

This document explains how MCP (Model Context Protocol) servers are integrated with LangGraph in this project.

## Architecture

### Process Separation

MCP servers run in **separate processes** from the main LangGraph server:

```
┌─────────────────────────────────────────┐
│   Main Process: LangGraph Server       │
│   (Port 2024)                           │
│                                         │
│   ┌───────────────────────────────┐    │
│   │  graph.py                     │    │
│   │  - Lazy MCP initialization    │    │
│   │  - Background pre-warming     │    │
│   └──────────┬────────────────────┘    │
│              │                          │
│              │ stdio/HTTP communication │
└──────────────┼──────────────────────────┘
               │
               ├──────────────────┐
               │                  │
         ┌─────▼──────┐    ┌─────▼──────┐      ┌──────────────┐
         │ Process 1  │    │ Process 2  │      │   HTTP       │
         │ manim_docs │    │ wikipedia  │      │   tavily     │
         │ MCP server │    │ MCP server │      │   MCP API    │
         └─────────── ┘    └────────────┘      └──────────────┘
```

### MCP Server Types

1. **stdio Transport (Subprocess)**

   - `manim_docs`: Custom Python MCP server running `mcp_server.py`
   - `wikipedia`: Wikipedia MCP server (`wikipedia-mcp` package)
   - **Communication**: stdin/stdout pipes
   - **Process**: Spawned as subprocess by `MultiServerMCPClient`

2. **HTTP Transport**
   - `tavily`: Tavily search API via MCP protocol
   - **Communication**: HTTP requests to `mcp.tavily.com`
   - **Process**: Remote server (no subprocess)

## Implementation Details

### Lazy Initialization

Tools are loaded **on first use**, not at module import:

```python
# Module load: graph is created synchronously
graph = build_graph()  # ✅ No async operations

# First agent run: MCP tools are initialized
async def call_agent(state):
    tools = await get_mcp_tools()  # ✅ Async initialization here
    ...
```

### Background Pre-Warming

To improve first-request performance, MCP connections are **pre-warmed in a background thread**:

```python
# When module loads, start background initialization
pre_warm_mcp_in_background()

# Background thread runs async initialization
def _background_init():
    asyncio.run(get_mcp_tools())  # Warms up connections
```

### Caching

MCP tools and clients are **cached globally** to avoid reconnecting:

```python
_tools_cache = None       # Cached list of tools
_client_cache = None      # Cached MCP client instance

# First call: Initialize and cache
# Subsequent calls: Return cached tools instantly
```

## Benefits

### 1. **Process Isolation**

- MCP servers crash → LangGraph server continues running
- Independent resource usage
- Clean separation of concerns

### 2. **Performance**

- Background pre-warming → Fast first request
- Caching → Instant subsequent requests
- Connection reuse → No repeated handshakes

### 3. **Development Experience**

- Server output separated from MCP server output
- Cleaner logs
- Easier debugging

## Configuration

MCP servers are configured in `graph.py`:

```python
MCP_CONFIG = {
    "manim_docs": {
        "transport": "stdio",
        "command": "python",
        "args": [MCP_SERVER_PATH],
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
```

## Process Lifecycle

### Startup Sequence

1. LangGraph imports `graph.py`
2. `pre_warm_mcp_in_background()` is called
3. Background thread starts MCP client initialization
4. MCP subprocesses are spawned:
   - `python mcp_server.py` (manim_docs)
   - `wikipedia-mcp --transport stdio` (wikipedia)
5. HTTP connection to Tavily is established
6. Tools are cached
7. Graph is ready for requests

### During Request

1. User sends message to agent
2. `call_agent()` calls `get_mcp_tools()`
3. Returns cached tools instantly (already initialized)
4. LLM bound with tools processes request
5. If tool needed, `call_tools()` executes via MCP

### Shutdown

1. User stops LangGraph server (Ctrl+C)
2. Python cleanup handlers run
3. MCP client connections close
4. MCP subprocess servers terminate
5. Clean shutdown

## Troubleshooting

### Issue: MCP servers not starting

**Symptoms**: Tools not loading, connection errors

**Check**:

```bash
# Verify mcp_server.py exists
ls src/agent/mcp_server.py

# Verify wikipedia-mcp is installed
wikipedia-mcp --help

# Check environment variables
echo $TAVILY_API_KEY
```

### Issue: Mixed output in logs

**Note**: The MCP server output (especially Wikipedia's fancy banner) appears in the same terminal as LangGraph. This is expected when using stdio transport.

**Why**: stdio servers communicate via stdin/stdout, and their stderr is visible in the parent process terminal.

### Issue: Slow first request

**Expected**: First request takes longer (~2-3 seconds) to initialize MCP connections

**Solution**: Already implemented! Background pre-warming runs at startup.

## Tools Available

The agent has access to **15 tools** across 3 MCP servers:

- **manim_docs**: Manim documentation search tools
- **wikipedia**: Wikipedia search and lookup
- **tavily**: Web search capabilities

Check available tools:

```python
tools = asyncio.run(get_mcp_tools())
print(f"Available tools: {len(tools)}")
for tool in tools:
    print(f"  - {tool.name}")
```

## Further Reading

- [MCP Protocol Specification](https://spec.modelcontextprotocol.io/)
- [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp)
- [FastMCP Documentation](https://gofastmcp.com/)
