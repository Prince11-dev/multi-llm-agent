import time
from openai import OpenAI
from app.config import settings

client = OpenAI(
    api_key=settings.DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)


async def ask_deepseek(
    question: str
):

    start = time.time()

    try:

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