from aiogram import Router, F
from aiogram.types import Message
from db import get_user, update_user_time
from services.economy import bonus_amount
from services.cooldown import check_cd
import time

router = Router()

@router.message(F.text.in_(["🎁 Бонус", "бонус"]))
async def bonus(msg: Message):
    user = get_user(msg.from_user.id)

    if not user:
        await msg.answer("Сначала получи карту")
        return

    if not check_cd(user[5], 86400):
        await msg.answer("⏳ Бонус уже получен")
        return

    amount = bonus_amount()

    from db import cursor, conn
    cursor.execute("UPDATE users SET diamonds=diamonds+? WHERE user_id=?",
                   (amount, msg.from_user.id))
    conn.commit()

    update_user_time(msg.from_user.id, "last_bonus", int(time.time()))

    await msg.answer(f"🎁 +{amount} 💎 алмазов")
