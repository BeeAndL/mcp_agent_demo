from mcp.server.fastmcp import FastMCP
from tools import host_operations

mcp = FastMCP("host_operations_mcp")
mcp.add_tool(host_operations.get_host_info)

if __name__ == "__main__":
    mcp.run("stdio")
