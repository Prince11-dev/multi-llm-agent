import time
from google import genai
from app.config import settings

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


async def ask_gemini(
    question: str
):

    start = time.time()

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        return {
            "provider": "gemini",
            "answer": response.text,
            "time": round(
                time.time() - start,
                2
            ),
            "success": True
        }

    except Exception as e:

        return {
            "provider": "gemini",
            "answer": str(e),
            "time": round(
                time.time() - start,
                2
            ),
            "success": False
        }