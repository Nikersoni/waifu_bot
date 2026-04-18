import asyncpg
from config import *

pool = None

async def init_db():
    global pool
    pool = await asyncpg.create_pool(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

async def get_pool():
    return pool
