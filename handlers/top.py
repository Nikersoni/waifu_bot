from aiogram import Router, F
from aiogram.types import Message
from db import pool

router = Router()


@router.message(F.text.in_(["топ"]))
async def top(msg: Message):

    async with pool.acquire() as conn:

        rows = await conn.fetch("""
            SELECT username, diamonds
            FROM users
            ORDER BY diamonds DESC
            LIMIT 5
        """)

    text = "🏆 ТОП\n\n"

    for i, r in enumerate(rows, 1):
        text += f"{i}. {r['username']} - {r['diamonds']} 💎\n"

    await msg.answer(text)
