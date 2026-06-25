from app.services.aggregator import aggregate


async def compare_models(
    question: str
):

    responses = await aggregate(
        question
    )

    return responses