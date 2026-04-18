from aiogram import Router, F
from aiogram.types import Message
from db import get_user, cursor

router = Router()

RARITY_EMOJI = {
    "common": "⚪",
    "rare": "🟢",
    "epic": "🔵",
    "legend": "🟣",
    "myth": "🟡"
}


@router.message(F.text.in_(["профиль", "👤 Профиль"]))
async def profile(msg: Message):

    user = get_user(msg.from_user.id)

    if not user:
        await msg.answer("Создай профиль через /start")
        return

    cursor.execute("""
    SELECT rarity, SUM(count)
    FROM inventory
    WHERE user_id=?
    GROUP BY rarity
    """, (msg.from_user.id,))

    rows = cursor.fetchall()

    stats = {
        "common": 0,
        "rare": 0,
        "epic": 0,
        "legend": 0,
        "myth": 0
    }

    total = 0

    for r in rows:
        stats[r[0]] = r[1]
        total += r[1]

    text = f"""👤 {user[1]}

📦 Коллекция
Всего: {total}

⚪ {stats['common']}  🟢 {stats['rare']}  🔵 {stats['epic']}  🟣 {stats['legend']}  🟡 {stats['myth']}

💎 Алмазы: {user[2]}
🧪 Пыль: {user[3]}
"""

    await msg.answer(text)
