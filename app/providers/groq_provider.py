import time
from groq import Groq
from app.config import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)


async def ask_groq(
    question: str
):

    start = time.time()

    try:
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