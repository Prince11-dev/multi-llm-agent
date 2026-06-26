import time
from google import genai

from app.config import settings


def get_client():
    """
    Create the Gemini client only when it is actually needed.
    This prevents import-time failures in CI environments where
    API keys are not configured.
    """
    if not settings.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not configured.")

    return genai.Client(
        api_key=settings.GEMINI_API_KEY
    )


async def ask_gemini(question: str):

    start = time.time()

    try:
        client = get_client()

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        return {
            "provider": "gemini",
            "answer": response.text,
            "time": round(time.time() - start, 2),
            "success": True
        }

    except Exception as e:

        return {
            "provider": "gemini",
            "answer": str(e),
            "time": round(time.time() - start, 2),
            "success": False
        }