from aiogram import Router, F
from aiogram.types import Message
from db import cursor

router = Router()


@router.message(F.text.in_(["инв", "инвентарь", "🎒 Инвентарь"]))
async def inv(msg: Message):

    cursor.execute("""
    SELECT card_name, rarity, count
    FROM inventory
    WHERE user_id=?
    """, (msg.from_user.id,))

    rows = cursor.fetchall()

    if not rows:
        await msg.answer("Пусто")
        return

    text = "🎒 Инвентарь\n\n"

    for r in rows:
        text += f"{r[0]} x{r[2]}\n"

    await msg.answer(text)
