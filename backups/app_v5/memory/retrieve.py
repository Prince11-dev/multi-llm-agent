import sqlite3

DB_NAME = "memory.db"


def get_history(
    session_id: str,
    limit: int = 3
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT question
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

    return [row[0] for row in rows]