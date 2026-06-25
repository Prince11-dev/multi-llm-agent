import asyncio
import time

from app.providers.gemini_provider import ask_gemini
from app.providers.groq_provider import ask_groq
from app.providers.deepseek_provider import ask_deepseek


async def timed_call(func, prompt: str):

    start = time.perf_counter()

    try:

        result = await func(prompt)

        return {
            "response": result,
            "time": round(time.perf_counter() - start, 2),
            "status": "success"
        }

    except Exception as e:

        return {
            "response": f"Provider Error: {str(e)}",
            "time": round(time.perf_counter() - start, 2),
            "status": "failed"
        }


async def aggregate(question: str):

    gemini_result, groq_result, deepseek_result = await asyncio.gather(
        timed_call(ask_gemini, question),
        timed_call(ask_groq, question),
        timed_call(ask_deepseek, question)
    )

    return {
        "gemini": gemini_result,
        "groq": groq_result,
        "deepseek": deepseek_result
    }