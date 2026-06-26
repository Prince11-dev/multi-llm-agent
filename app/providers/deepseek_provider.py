import time

from openai import OpenAI

from app.config import settings


def get_client():
    """
    Create the DeepSeek client only when needed.

    This prevents import-time failures in CI environments
    where API keys are intentionally not configured.
    """

    if not settings.DEEPSEEK_API_KEY:
        raise ValueError("DEEPSEEK_API_KEY is not configured.")

    return OpenAI(
        api_key=settings.DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com"
    )


async def ask_deepseek(question: str):

    start = time.time()

    try:

        client = get_client()

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response.choices[0].message.content

        return {
            "provider": "deepseek",
            "answer": answer,
            "time": round(
                time.time() - start,
                2
            ),
            "success": True
        }

    except Exception as e:

        return {
            "provider": "deepseek",
            "answer": str(e),
            "time": round(
                time.time() - start,
                2
            ),
            "success": False
        }