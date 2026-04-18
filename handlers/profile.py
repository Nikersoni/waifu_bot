from aiogram import Router, F
from aiogram.types import Message
from db import get_user, cursor

router = Router()


@router.message(F.text.in_(["профиль", "👤 Профиль"]))
async def profile(msg: Message):

    user = get_user(msg.from_user.id)

    cursor.execute("SELECT COUNT(*) FROM inventory WHERE user_id=?",
                   (msg.from_user.id,))

    cards = cursor.fetchone()[0]

    await msg.answer(
f"""👤 {msg.from_user.username}

💎 Алмазы: {user[2]}
🧪 Пыль: {user[3]}
🎴 Карточек: {cards}
"""
    )
