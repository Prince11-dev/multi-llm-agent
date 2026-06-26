import time

from openai import OpenAI

from app.config import settings


def get_client():
    """
    Create the OpenAI client only when needed.

    This prevents import-time failures in CI environments
    where API keys are intentionally not configured.
    """

    if not settings.OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not configured.")

    return OpenAI(
        api_key=settings.OPENAI_API_KEY
    )


async def ask_openai(question: str):

    start = time.time()

    try:

        client = get_client()

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response.choices[0].message.content

        return {
            "provider": "openai",
            "answer": answer,
            "time": round(
                time.time() - start,
                2
            ),
            "success": True
        }

    except Exception as e:

        return {
            "provider": "openai",
            "answer": str(e),
            "time": round(
                time.time() - start,
                2
            ),
            "success": False
        }