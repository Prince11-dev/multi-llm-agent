import time
from openai import OpenAI
from app.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


async def ask_openai(
    question: str
):

    start = time.time()

    try:

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