from app.providers.deepseek_provider import ask_deepseek

async def synthesize(question: str, responses: dict):

    valid_answers = []

    for provider in responses.values():

        if provider["status"] == "success":
            valid_answers.append(
                provider["response"]
            )

    combined_answers = "\n\n".join(valid_answers)

    prompt = f"""
Question:
{question}

Answers:
{combined_answers}

Instructions:
- Compare the answers
- Remove duplicate information
- Keep strongest reasoning
- Keep factual accuracy
- Produce one superior final answer
- Return only the final answer
"""

    return await ask_deepseek(prompt)