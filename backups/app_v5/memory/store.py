import sqlite3

DB_NAME = "memory.db"


def save_conversation(
    session_id: str,
    question: str,
    answer: str
):

    conn = sqlite3.connect(DB_NAME)

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