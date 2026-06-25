from groq import AsyncGroq

from app.config import GROQ_API_KEY

client = AsyncGroq(
    api_key=GROQ_API_KEY
)


async def ask_groq(prompt: str):

    response = await client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content