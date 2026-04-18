from aiogram import Router
from aiogram.types import Message
import time

from db import pool
from services.cards import roll_card
from services.cooldown import check_cd
from config import CARD_COOLDOWN

router = Router()

RARITY_EMOJI = {
    "common": "⚪",
    "rare": "🟢",
    "epic": "🔵",
    "legend": "🟣",
    "myth": "🟡"
}


@router.message(F.text)
async def card(msg: Message):

    text = (msg.text or "").lower().strip()

    if text not in ["карта", "🎴 карта", "/карта"]:
        return

    async with pool.acquire() as conn:

        user = await conn.fetchrow(
            "SELECT * FROM users WHERE user_id=$1",
            msg.from_user.id
        )

        if not user:
            await conn.execute("""
                INSERT INTO users (user_id, username)
                VALUES ($1,$2)
            """, msg.from_user.id, msg.from_user.username)

            user = await conn.fetchrow(
                "SELECT * FROM users WHERE user_id=$1",
                msg.from_user.id
            )

        if not check_cd(user["last_card"], CARD_COOLDOWN):
            await msg.answer("⏳ КД 24 часа")
            return

        card_name, rarity = roll_card()

        await conn.execute("""
            INSERT INTO inventory (user_id, card_name, rarity, count)
            VALUES ($1,$2,$3,1)
            ON CONFLICT(user_id, card_name)
            DO UPDATE SET count = inventory.count + 1
        """, msg.from_user.id, card_name, rarity)

        await conn.execute("""
            UPDATE users
            SET active_name=$1,
                active_rarity=$2,
                active_level=1,
                active_hp=100,
                last_card=$3
            WHERE user_id=$4
        """, card_name, rarity, int(time.time()), msg.from_user.id)

    await msg.answer(
f"""✨ ТЕБЕ ВЫПАЛА ВАЙФУ!

{RARITY_EMOJI[rarity]} {card_name}"""
    )
