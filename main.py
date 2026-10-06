from fastmcp import FastMCP
from fastapi import FastAPI

mcp = FastMCP("first MCP server")
app = FastAPI(title="addtion app ")

@app.post('/addition')
def add(a: int, b: int) -> int:
    '''Addition of two numbers'''
    return a+b

    