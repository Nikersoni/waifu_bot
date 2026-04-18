import asyncpg
from config import DATABASE_URL

pool = None


async def init_db():
    global pool

    pool = await asyncpg.create_pool(DATABASE_URL)

    async with pool.acquire() as conn:

        await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            username TEXT,
            diamonds BIGINT DEFAULT 0,
            dust BIGINT DEFAULT 0,
            streak INT DEFAULT 0,
            last_streak_date DATE,
            last_card TIMESTAMP,
            last_bonus TIMESTAMP,
            active_name TEXT,
            active_rarity TEXT,
            active_level INT DEFAULT 1,
            active_hp INT
        );
        """)

        await conn.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            user_id BIGINT,
            card_name TEXT,
            rarity TEXT,
            count INT DEFAULT 1,
            PRIMARY KEY (user_id, card_name)
        );
        """)


async def get_pool():
    return pool


async def get_or_create_user(user_id: int, username: str):
    async with pool.acquire() as conn:

        user = await conn.fetchrow(
            "SELECT * FROM users WHERE user_id = $1",
            user_id
        )

        if not user:
            await conn.execute("""
                INSERT INTO users (user_id, username)
                VALUES ($1, $2)
            """, user_id, username)
