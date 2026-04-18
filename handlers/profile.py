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

    user_id = user[0]
    username = user[1]
    diamonds = user[2]
    dust = user[3]

    # 📦 статистика коллекции
    cursor.execute("""
    SELECT rarity, SUM(count)
    FROM inventory
    WHERE user_id=?
    GROUP BY rarity
    """, (user_id,))

    rows = cursor.fetchall()

    stats = {
        "common": 0,
        "rare": 0,
        "epic": 0,
        "legend": 0,
        "myth": 0
    }

    total_cards = 0

    for r in rows:
        stats[r[0]] = r[1]
        total_cards += r[1]

    # 🏆 заглушки рейтинга (пока без системы)
    balance_rank = "#7"
    collection_rank = "#5"

    text = f"""👤 @{username}
ID: {user_id}

━━━━━━━━━━━━━━━
💎 Кристаллы: {diamonds:,}
📅 Стрик: 5 дней

━━━━━━━━━━━━━━━
💍 Активная вайфу:
🟣 Аянами Рей
Lv.1 ❤️ 100

Бонус: скоро
━━━━━━━━━━━━━━━
📦 Коллекция:
Всего: {total_cards}

⚪ {stats['common']}  🟢 {stats['rare']}  🔵 {stats['epic']}  🟣 {stats['legend']}  🟡 {stats['myth']}

━━━━━━━━━━━━━━━
🏆 Позиции:
Баланс: {balance_rank}
Коллекция: {collection_rank}
"""

    await msg.answer(text)
