from openai import AsyncOpenAI

from app.config import OPENROUTER_API_KEY

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


async def ask_deepseek(prompt: str):

    try:

        response = await client.chat.completions.create(
            model="deepseek/deepseek-r1",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=800,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Provider Error: {str(e)}"