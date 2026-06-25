from app.providers.groq_provider import ask_groq


async def synthesize(
    question: str,
    responses: dict
):

    successful = []

    for provider, data in responses.items():

        if data.get("success"):

            successful.append(
                f"""
Provider: {provider}

Answer:
{data['answer']}
"""
            )

    if not successful:
        return "No providers returned a successful response."

    if len(successful) == 1:
        return responses[
            next(
                k for k, v in responses.items()
                if v.get("success")
            )
        ]["answer"]

    prompt = f"""
Question:
{question}

Multiple AI models answered this question.

{' '.join(successful)}

Combine the answers into one final response.
"""

    result = await ask_groq(
        prompt
    )

    return result["answer"]