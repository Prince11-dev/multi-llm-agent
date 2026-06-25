async def intelligent_route(
    question: str
):

    question = question.lower()

    if any(
        word in question
        for word in [
            "code",
            "python",
            "fastapi",
            "bug",
            "error"
        ]
    ):
        return "groq"

    if any(
        word in question
        for word in [
            "essay",
            "creative",
            "story",
            "blog"
        ]
    ):
        return "gemini"

    return "groq"