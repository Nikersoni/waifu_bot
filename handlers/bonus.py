from aiogram import Router, F
from aiogram.types import Message
import time

from db import pool
from services.economy import bonus_amount
from services.cooldown import check_cd
from config import BONUS_COOLDOWN

router = Router()


@router.message(F.text.in_(["бонус"]))
async def bonus(msg: Message):

    async with pool.acquire() as conn:

        user = await conn.fetchrow(
            "SELECT * FROM users WHERE user_id=$1",
            msg.from_user.id
        )

        if not check_cd(user["last_bonus"], BONUS_COOLDOWN):
            await msg.answer("⏳ КД бонус")
            return

        amount = bonus_amount()

        await conn.execute("""
            UPDATE users
            SET diamonds = diamonds + $1,
                last_bonus = $2
            WHERE user_id = $3
        """, amount, int(time.time()), msg.from_user.id)

    await msg.answer(f"🎁 +{amount} 💎")
