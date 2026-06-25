async def route_question(question: str):

    question_lower = question.lower()

    coding_keywords = [
        "code",
        "python",
        "java",
        "bug",
        "debug",
        "algorithm",
        "fastapi",
        "api",
        "sql",
        "database",
        "react",
        "django"
    ]

    research_keywords = [
        "research",
        "compare",
        "analysis",
        "advantages",
        "disadvantages",
        "study"
    ]

    for keyword in coding_keywords:
        if keyword in question_lower:
            return "deepseek"

    for keyword in research_keywords:
        if keyword in question_lower:
            return "gemini"

    return "groq"