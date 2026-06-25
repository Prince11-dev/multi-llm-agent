from app.providers.deepseek_provider import ask_deepseek


async def intelligent_route(question: str):

    prompt = f"""
Classify this question into ONE category only.

Categories:

- coding
- research
- general
- complex
- search

Use search when the question asks about:

- latest news
- current events
- recent updates
- trending topics
- today's information
- live information
- current technologies
- recent AI releases

Question:

{question}

Return only category name.
"""

    try:

        route = await ask_deepseek(
            prompt
        )

        route = route.strip().lower()

        if "search" in route:
            return "search"

        if "coding" in route:
            return "coding"

        if "research" in route:
            return "research"

        if "complex" in route:
            return "complex"

        return "general"

    except Exception:

        return "general"