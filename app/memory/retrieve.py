from app.memory.database import get_connection


def get_history(
    session_id: str,
    limit: int = 10
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT question, answer
        FROM conversations
        WHERE session_id = ?
        ORDER BY id DESC
        LIMIT ?
        """,
        (
            session_id,
            limit
        )
    )

    rows = cursor.fetchall()

    conn.close()

    history = []

    for row in rows:

        history.append(
            {
                "question": row[0],
                "answer": row[1]
            }
        )

    return history