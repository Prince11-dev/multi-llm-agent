from app.services.intelligent_executor import (
    intelligent_execute
)


async def stream_answer(
    question: str
):

    return await intelligent_execute(
        "groq",
        question
    )