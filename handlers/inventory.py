from aiogram import Router, F
from aiogram.types import Message
from db import pool

router = Router()


@router.message(F.text.in_(["инв", "инвентарь"]))
async def inv(msg: Message):

    async with pool.acquire() as conn:

        rows = await conn.fetch("""
            SELECT card_name, rarity, count
            FROM inventory
            WHERE user_id=$1
        """, msg.from_user.id)

    if not rows:
        await msg.answer("Пусто")
        return

    text = "🎒 Инвентарь\n\n"

    for r in rows:
        text += f"{r['card_name']} x{r['count']}\n"

    await msg.answer(text)
