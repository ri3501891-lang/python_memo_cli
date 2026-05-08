import sqlite3
from datetime import datetime

DB_NAME = "memo.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_memo(content):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO memos (content, created_at) VALUES (?, ?)",
        (content, created_at)
    )

    conn.commit()
    conn.close()


def get_memos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, content, created_at FROM memos")
    memos = cursor.fetchall()

    conn.close()
    return memos


def delete_memo(memo_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM memos WHERE id = ?", (memo_id,))

    conn.commit()
    conn.close()