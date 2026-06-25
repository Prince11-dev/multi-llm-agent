import asyncio
from app.providers.deepseek_provider import ask_deepseek

async def main():

    response = await ask_deepseek(
        "What is FastAPI?"
    )

    print("\n")
    print(response)
    print("\n")

asyncio.run(main())