import asyncio

from app.providers.groq_provider import ask_groq
from app.providers.gemini_provider import ask_gemini
from app.providers.deepseek_provider import ask_deepseek


async def aggregate(
    question: str
):

    tasks = [
        ask_groq(question),
        ask_gemini(question),
        ask_deepseek(question)
    ]

    results = await asyncio.gather(
        *tasks,
        return_exceptions=True
    )

    providers = [
        "groq",
        "gemini",
        "deepseek"
    ]

    responses = {}

    for provider, result in zip(
        providers,
        results
    ):

        if isinstance(
            result,
            Exception
        ):
            responses[provider] = {
                "provider": provider,
                "answer": str(result),
                "success": False,
                "time": 0
            }

        else:
            responses[provider] = result

    return responses