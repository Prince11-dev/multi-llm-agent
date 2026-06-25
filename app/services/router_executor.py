from app.providers.groq_provider import ask_groq
from app.providers.gemini_provider import ask_gemini
from app.providers.deepseek_provider import ask_deepseek


async def execute_route(
    model: str,
    question: str
):

    if model == "groq":
        return await ask_groq(
            question
        )

    if model == "gemini":
        return await ask_gemini(
            question
        )

    if model == "deepseek":
        return await ask_deepseek(
            question
        )

    return {
        "answer":
        "Unknown model"
    }