from app.providers.deepseek_provider import ask_deepseek
from app.providers.groq_provider import ask_groq

from app.services.aggregator import aggregate
from app.services.synthesizer import synthesize

from app.tools.web_search import search_web


async def intelligent_execute(
    route: str,
    question: str,
    context: str = ""
):

    enhanced_question = f"""
Conversation Context:

{context}

Current User Question:

{question}

Instructions:

1. Use conversation context when relevant.
2. Ignore irrelevant context.
3. Answer accurately.
4. Be concise unless detailed explanation is requested.
"""

    if route == "search":

        results = await search_web(question)

        search_context = ""

        for result in results:

            search_context += f"""
Title:
{result['title']}

Content:
{result['body']}

Source:
{result['href']}

"""

        search_prompt = f"""
Answer the user question using the search results.

Question:

{question}

Search Results:

{search_context}

Provide a clear answer.
"""

        return await ask_deepseek(
            search_prompt
        )

    elif route == "coding":

        return await ask_deepseek(
            enhanced_question
        )

    elif route == "research":

        return await ask_deepseek(
            enhanced_question
        )

    elif route == "complex":

        responses = await aggregate(
            enhanced_question
        )

        return await synthesize(
            enhanced_question,
            responses
        )

    return await ask_groq(
        enhanced_question
    )