from app.services.router_executor import execute_route


async def intelligent_execute(
    model: str,
    question: str,
    context: str = ""
):

    prompt = f"""
Conversation History:
{context}

Current Question:
{question}
"""

    result = await execute_route(
        model,
        prompt
    )

    return result["answer"]