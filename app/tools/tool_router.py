from app.tools.web_search import search_web
from app.tools.calculator import calculate
from app.tools.weather import get_weather


async def execute_tool(
    tool: str,
    value: str
):

    if tool == "search":
        return await search_web(
            value
        )

    if tool == "calculator":
        return await calculate(
            value
        )

    if tool == "weather":
        return await get_weather(
            value
        )

    return {
        "success": False,
        "error": "Unknown tool"
    }