from aiogram import Router, F
from aiogram.types import Message
from db import cursor

router = Router()


@router.message(F.text.lower().in_(["топ", "/топ", "🏆 топ", "top"]))
async def top(msg: Message):

    cursor.execute("""
    SELECT username, diamonds
    FROM users
    ORDER BY diamonds DESC
    LIMIT 5
    """)

    rows = cursor.fetchall()

    if not rows:
        await msg.answer("🏆 ТОП пуст")
        return

    text = "🏆 ТОП игроков\n\n"

    for i, r in enumerate(rows, 1):
        name = r[0] if r[0] else "Unknown"
        text += f"{i}. {name} — {r[1]} 💎\n"

    await msg.answer(text)
