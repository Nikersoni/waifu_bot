from aiogram import Router, F
from aiogram.types import Message
from db import get_user, update_user_time, cursor, conn
from services.economy import bonus_amount
from services.cooldown import check_cd
import time

router = Router()


@router.message(F.text.in_(["бонус", "🎁 Бонус"]))
async def bonus(msg: Message):

    user = get_user(msg.from_user.id)

    if not check_cd(user[5], 86400):
        await msg.answer("⏳ КД бонус")
        return

    amount = bonus_amount()

    cursor.execute("UPDATE users SET diamonds=diamonds+? WHERE user_id=?",
                   (amount, msg.from_user.id))
    conn.commit()

    update_user_time(msg.from_user.id, "last_bonus", int(time.time()))

    await msg.answer(f"🎁 +{amount} 💎")
