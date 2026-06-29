from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("Hidden Gems MCP")


@mcp.tool()
def hello() -> str:
    """Simple test tool."""
    return "🎵 Hello from Hidden Gems MCP!"


if __name__ == "__main__":
    mcp.run()