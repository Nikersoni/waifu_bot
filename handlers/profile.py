from aiogram import Router, F
from aiogram.types import Message
from db import get_user

router = Router()

@router.message(F.text.in_(["👤 Профиль", "профиль"]))
async def profile(msg: Message):
    user = get_user(msg.from_user.id)

    if not user:
        await msg.answer("Нет профиля")
        return

    await msg.answer(
f"""👤 {msg.from_user.username}

💎 Алмазы: {user[2]}
🧪 Пыль: {user[3]}
"""
    )
