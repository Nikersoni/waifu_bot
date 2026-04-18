import asyncio
import asyncpg
import os

DATABASE_URL = os.getenv("DATABASE_URL")

pool = None


async def init_db():
    global pool

    pool = await asyncpg.create_pool(DATABASE_URL)

    async with pool.acquire() as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            username TEXT,
            diamonds INT DEFAULT 0,
            dust INT DEFAULT 0,
            last_card BIGINT DEFAULT 0,
            last_bonus BIGINT DEFAULT 0,

            active_name TEXT,
            active_rarity TEXT,
            active_level INT DEFAULT 1,
            active_hp INT DEFAULT 100
        )
        """)

        await conn.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            user_id BIGINT,
            card_name TEXT,
            rarity TEXT,
            count INT DEFAULT 1,
            PRIMARY KEY (user_id, card_name)
        )
        """)


async def get_user(user_id):
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            "SELECT * FROM users WHERE user_id=$1",
            user_id
        )


async def create_user(user_id, username):
    async with pool.acquire() as conn:
        await conn.execute("""
        INSERT INTO users (user_id, username)
        VALUES ($1,$2)
        ON CONFLICT (user_id) DO NOTHING
        """, user_id, username)


async def update_user_time(user_id, field, value):
    async with pool.acquire() as conn:
        await conn.execute(f"""
        UPDATE users
        SET {field}=$1
        WHERE user_id=$2
        """, value, user_id)
