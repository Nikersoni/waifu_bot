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

    # 📦 коллекция
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

    total = 0

    for r in rows:
        stats[r[0]] = r[1]
        total += r[1]

    # 🏆 реальный топ (баланс)
    cursor.execute("""
    SELECT user_id, username, diamonds
    FROM users
    ORDER BY diamonds DESC
    """)
    all_users = cursor.fetchall()

    balance_rank = 0
    for i, u in enumerate(all_users, 1):
        if u[0] == user_id:
            balance_rank = i
            break

    # 📊 топ коллекции
    cursor.execute("""
    SELECT user_id, SUM(count) as total
    FROM inventory
    GROUP BY user_id
    ORDER BY total DESC
    """)
    col = cursor.fetchall()

    collection_rank = 0
    for i, u in enumerate(col, 1):
        if u[0] == user_id:
            collection_rank = i
            break

    # 💍 активная вайфу
    active_name = user[6]
    active_rarity = user[7]
    active_level = user[8]
    active_hp = user[9]

    active_text = "Нет"
    if active_name:
        active_text = f"{RARITY_EMOJI.get(active_rarity, '⚪')} {active_name}\nLv.{active_level} ❤️ {active_hp}"

    text = f"""👤 @{user[1]}
ID: {user_id}

━━━━━━━━━━━━━━━
💎 Кристаллы: {user[2]}
📅 Стрик: 0 дней

━━━━━━━━━━━━━━━
💍 Активная вайфу:
{active_text}

Бонус: скоро
━━━━━━━━━━━━━━━
📦 Коллекция:
Всего: {total}

⚪ {stats['common']}  🟢 {stats['rare']}  🔵 {stats['epic']}  🟣 {stats['legend']}  🟡 {stats['myth']}

━━━━━━━━━━━━━━━
🏆 Позиции:
Баланс: #{balance_rank}
Коллекция: #{collection_rank}
"""

    await msg.answer(text)
