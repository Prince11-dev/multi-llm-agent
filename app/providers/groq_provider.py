import time

from groq import Groq

from app.config import settings


def get_client():
    """
    Create the Groq client only when needed.

    This prevents GitHub Actions and unit tests from failing
    during module import when no API key is configured.
    """

    if not settings.GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not configured.")

    return Groq(
        api_key=settings.GROQ_API_KEY
    )


async def ask_groq(question: str):

    start = time.time()

    try:

        client = get_client()

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response.choices[0].message.content

        return {
            "provider": "groq",
            "answer": answer,
            "time": round(
                time.time() - start,
                2
            ),
            "success": True
        }

    except Exception as e:

        return {
            "provider": "groq",
            "answer": str(e),
            "time": round(
                time.time() - start,
                2
            ),
            "success": False
        }