from aiogram import Router, F
from aiogram.types import Message
from db import cursor

router = Router()


@router.message(F.text == "топ")
async def top(msg: Message):

    cursor.execute("SELECT username, diamonds FROM users ORDER BY diamonds DESC LIMIT 5")
    rows = cursor.fetchall()

    text = "🏆 ТОП\n\n"

    for i, r in enumerate(rows, 1):
        text += f"{i}. {r[0]} - {r[1]} 💎\n"

    await msg.answer(text)
