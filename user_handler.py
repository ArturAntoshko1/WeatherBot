import sqlite3

from aiogram import types


def save_user(message: types.Message):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER UNIQUE,
            first_name TEXT NOT NULL,
            username TEXT
        )
        """)

        cursor.execute(
            """INSERT INTO users(id, first_name, username) VALUES(?, ?, ?)""",
        (message.chat.id, message.from_user.first_name, message.from_user.username)
        )
    except sqlite3.Error as error:
        print(error)
    finally:
        conn.commit()
        conn.close()