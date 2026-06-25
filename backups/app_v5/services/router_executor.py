from app.providers.groq_provider import ask_groq
from app.providers.deepseek_provider import ask_deepseek
from app.providers.gemini_provider import ask_gemini


async def execute_route(
    route: str,
    question: str
):

    if route == "deepseek":
        return await ask_deepseek(question)

    if route == "gemini":
        return await ask_gemini(question)

    return await ask_groq(question)