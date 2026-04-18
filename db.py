import asyncpg
from config import *

pool: asyncpg.Pool | None = None


async def init_db():
    global pool

    pool = await asyncpg.create_pool(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        min_size=1,
        max_size=10
    )

    await create_tables()


async def get_pool():
    return pool


async def create_tables():
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
