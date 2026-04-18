import sqlite3
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/bot.db", check_same_thread=False)
cursor = conn.cursor()


def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        diamonds INTEGER DEFAULT 0,
        dust INTEGER DEFAULT 0,
        last_card INTEGER DEFAULT 0,
        last_bonus INTEGER DEFAULT 0,

        active_name TEXT DEFAULT NULL,
        active_rarity TEXT DEFAULT NULL,
        active_level INTEGER DEFAULT 1,
        active_hp INTEGER DEFAULT 100
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        user_id INTEGER,
        card_name TEXT,
        rarity TEXT,
        count INTEGER DEFAULT 1,
        PRIMARY KEY (user_id, card_name)
    )
    """)

    conn.commit()


def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    return cursor.fetchone()


def create_user(user_id, username):
    cursor.execute("""
    INSERT OR IGNORE INTO users (user_id, username)
    VALUES (?,?)
    """, (user_id, username))
    conn.commit()


def update_user_time(user_id, field, value):
    cursor.execute(f"""
    UPDATE users
    SET {field}=?
    WHERE user_id=?
    """, (value, user_id))
    conn.commit()
