"""MCP Filesystem Tools Server for Manim Agent.

This module provides FastMCP-based filesystem tools that can be loaded
via MCP protocol for use with LangGraph agents.
"""

import os
import re
import subprocess
from pathlib import Path
from datetime import datetime

from fastmcp import FastMCP

# # Workspace Configuration
WORKSPACE_ROOT = Path("/home/aditya-ladawa/Aditya/z_projects/mathbox2/manim_workspace")
WORKSPACE_ROOT.mkdir(parents=True, exist_ok=True)

# Create subdirectories
(WORKSPACE_ROOT / "scenes").mkdir(exist_ok=True)
(WORKSPACE_ROOT / "assets").mkdir(exist_ok=True)


# # FastMCP Server
mcp = FastMCP(name="ManimFilesystem")


# # Security Helpers

def _ensure_safe_path(path: str) -> Path:
    """Ensure path is within workspace and return absolute Path."""
    vpath = path if path.startswith("/") else "/" + path
    
    if ".." in vpath or vpath.startswith("~"):
        raise ValueError("Path traversal not allowed")
    
    full_path = (WORKSPACE_ROOT / vpath.lstrip("/")).resolve()
    
    try:
        full_path.relative_to(WORKSPACE_ROOT)
    except ValueError:
        raise ValueError(f"Access denied: {path} is outside workspace") from None
    
    return full_path


def _format_with_line_numbers(content: str, start_line: int = 1) -> str:
    """Format content with line numbers."""
    lines = content.splitlines()
    result = []
    for i, line in enumerate(lines, start=start_line):
        result.append(f"{i:6d}\t{line}")
    return "\n".join(result)


# # Filesystem MCP Tools

@mcp.tool()
async def list_files(path: str = "/") -> list[dict]:
    """List files and directories in the specified path.
    
    Args:
        path: Directory path to list (default: "/")
        
    Returns:
        List of file/directory info dicts with path, is_dir, size, modified_at
    """
    try:
        dir_path = _ensure_safe_path(path)
        
        if not dir_path.exists() or not dir_path.is_dir():
            return []
        
        results = []
        for item in sorted(dir_path.iterdir()):
            try:
                is_file = item.is_file()
                is_dir = item.is_dir()
                
                rel_path = "/" + str(item.relative_to(WORKSPACE_ROOT))
                if is_dir:
                    rel_path += "/"
                
                stat = item.stat()
                results.append({
                    "path": rel_path,
                    "is_dir": is_dir,
                    "size": stat.st_size if is_file else 0,
                    "modified_at": datetime.fromtimestamp(stat.st_mtime).isoformat()
                })
            except OSError:
                continue
        
        return results
    except ValueError as e:
        return [{"error": str(e)}]


@mcp.tool()
async def read_file(path: str, offset: int = 0, limit: int = 2000) -> str:
    """Read file content with line numbers.
    
    Args:
        path: File path to read
        offset: Line offset to start from (0-indexed)
        limit: Maximum number of lines to read
        
    Returns:
        Formatted file content with line numbers, or error message
    """
    try:
        file_path = _ensure_safe_path(path)
        
        if not file_path.exists() or not file_path.is_file():
            return f"Error: File '{path}' not found"
        
        content = file_path.read_text(encoding="utf-8")
        
        if not content or content.strip() == "":
            return "File exists but has empty contents"
        
        lines = content.splitlines()
        start_idx = offset
        end_idx = min(start_idx + limit, len(lines))
        
        if start_idx >= len(lines):
            return f"Error: Line offset {offset} exceeds file length ({len(lines)} lines)"
        
        selected_lines = lines[start_idx:end_idx]
        return _format_with_line_numbers("\n".join(selected_lines), start_line=start_idx + 1)
        
    except ValueError as e:
        return f"Error: {e}"
    except (OSError, UnicodeDecodeError) as e:
        return f"Error reading file '{path}': {e}"


@mcp.tool()
async def write_file(path: str, content: str) -> str:
    """Create a new file with content.
    
    Args:
        path: File path to create
        content: File content to write
        
    Returns:
        Success message or error
    """
    try:
        file_path = _ensure_safe_path(path)
        
        if file_path.exists():
            return f"Error: Cannot write to {path} because it already exists. Use edit_file to modify existing files."
        
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")
        
        return f"Successfully wrote to {path}"
        
    except ValueError as e:
        return f"Error: {e}"
    except (OSError, UnicodeEncodeError) as e:
        return f"Error writing file '{path}': {e}"


@mcp.tool()
async def edit_file(path: str, old_string: str, new_string: str, replace_all: bool = False) -> str:
    """Edit a file by replacing string occurrences.
    
    Args:
        path: File path to edit
        old_string: String to replace
        new_string: Replacement string
        replace_all: Whether to replace all occurrences (default: False)
        
    Returns:
        Success message with occurrence count, or error
    """
    try:
        file_path = _ensure_safe_path(path)
        
        if not file_path.exists() or not file_path.is_file():
            return f"Error: File '{path}' not found"
        
        content = file_path.read_text(encoding="utf-8")
        occurrences = content.count(old_string)
        
        if occurrences == 0:
            return f"Error: String not found in file: '{old_string}'"
        
        if occurrences > 1 and not replace_all:
            return f"Error: String '{old_string}' appears {occurrences} times. Set replace_all=True to replace all, or provide more specific context."
        
        new_content = content.replace(old_string, new_string)
        file_path.write_text(new_content, encoding="utf-8")
        
        return f"Successfully edited {path} ({occurrences} occurrence(s) replaced)"
        
    except ValueError as e:
        return f"Error: {e}"
    except (OSError, UnicodeDecodeError, UnicodeEncodeError) as e:
        return f"Error editing file '{path}': {e}"


@mcp.tool()
async def search_files(pattern: str, path: str = "/", file_pattern: str | None = None) -> str:
    """Search file contents for regex pattern (grep).
    
    Args:
        pattern: Regex pattern to search for
        path: Base path to search from (default: "/")
        file_pattern: Optional glob pattern to filter files (e.g., "*.py")
        
    Returns:
        Formatted search results showing file:line:content, or error
    """
    try:
        try:
            regex = re.compile(pattern)
        except re.error as e:
            return f"Invalid regex pattern: {e}"
        
        base_path = _ensure_safe_path(path)
        
        if not base_path.exists():
            return "No matches found"
        
        results = []
        search_root = base_path if base_path.is_dir() else base_path.parent
        
        for file_path in search_root.rglob("*"):
            if not file_path.is_file():
                continue
            
            if file_pattern and not file_path.match(file_pattern):
                continue
            
            try:
                content = file_path.read_text(encoding="utf-8")
                for line_num, line in enumerate(content.splitlines(), 1):
                    if regex.search(line):
                        virt_path = "/" + str(file_path.relative_to(WORKSPACE_ROOT))
                        results.append(f"{virt_path}:{line_num}: {line}")
            except (UnicodeDecodeError, PermissionError, OSError):
                continue
        
        if not results:
            return "No matches found"
        
        return "\n".join(results[:100])
        
    except ValueError as e:
        return f"Error: {e}"


@mcp.tool()
async def find_files(pattern: str, path: str = "/") -> str:
    """Find files matching glob pattern.
    
    Args:
        pattern: Glob pattern (e.g., "*.py", "**/*.ts")
        path: Base path to search from (default: "/")
        
    Returns:
        Newline-separated list of matching file paths, or error
    """
    try:
        search_path = _ensure_safe_path(path)
        
        if not search_path.exists() or not search_path.is_dir():
            return "No files found"
        
        matches = []
        for file_path in search_path.rglob(pattern):
            if file_path.is_file():
                virt_path = "/" + str(file_path.relative_to(WORKSPACE_ROOT))
                stat = file_path.stat()
                matches.append((virt_path, stat.st_mtime))
        
        if not matches:
            return "No files found"
        
        matches.sort(key=lambda x: x[1], reverse=True)
        
        return "\n".join(path for path, _ in matches)
        
    except ValueError as e:
        return f"Error: {e}"


@mcp.tool()
async def execute_command(command: str, timeout: int = 300) -> dict:
    """Execute a shell command in the workspace directory.
    
    Args:
        command: Command to execute (e.g., "manim render scenes/intro.py -ql")
        timeout: Maximum execution time in seconds (default: 300)
        
    Returns:
        Dict with stdout, stderr, and exit_code
    """
    allowed_commands = ["manim", "python", "ls", "cat"]
    cmd_parts = command.split()
    
    if not cmd_parts or not any(cmd_parts[0].startswith(allowed) for allowed in allowed_commands):
        return {
            "stdout": "",
            "stderr": f"Error: Command not allowed: {cmd_parts[0] if cmd_parts else 'empty'}",
            "exit_code": 1
        }
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=str(WORKSPACE_ROOT),
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode
        }
        
    except subprocess.TimeoutExpired:
        return {
            "stdout": "",
            "stderr": f"Error: Command timed out after {timeout} seconds",
            "exit_code": 124
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": f"Error executing command: {e}",
            "exit_code": 1
        }


# Run MCP server if executed directly
if __name__ == "__main__":
    mcp.run()
