async def route_question(
    question: str
):

    question = question.lower()

    if any(
        word in question
        for word in [
            "code",
            "python",
            "programming",
            "debug"
        ]
    ):
        return "groq"

    if any(
        word in question
        for word in [
            "creative",
            "write",
            "story",
            "poem"
        ]
    ):
        return "gemini"

    return "groq"