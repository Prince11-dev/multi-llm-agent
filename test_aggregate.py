import asyncio
from app.services.aggregator import aggregate


async def main():

    response = await aggregate(
        "What is FastAPI?"
    )

    print(response)


asyncio.run(main())