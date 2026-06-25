from app.memory.database import get_connection


def save_conversation(
    session_id: str,
    question: str,
    answer: str
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO conversations
        (
            session_id,
            question,
            answer
        )
        VALUES (?, ?, ?)
        """,
        (
            session_id,
            question,
            answer
        )
    )

    conn.commit()
    conn.close()