from aiogram import Router, F
from aiogram.types import Message
from db import pool

router = Router()


@router.message(F.text.in_(["профиль", "👤 профиль"]))
async def profile(msg: Message):

    async with pool.acquire() as conn:

        user = await conn.fetchrow(
            "SELECT * FROM users WHERE user_id=$1",
            msg.from_user.id
        )

        if not user:
            await msg.answer("Создай профиль /start")
            return

        # 📦 коллекция
        rows = await conn.fetch("""
            SELECT rarity, SUM(count) as c
            FROM inventory
            WHERE user_id=$1
            GROUP BY rarity
        """, msg.from_user.id)

        stats = {
            "common": 0,
            "rare": 0,
            "epic": 0,
            "legend": 0,
            "myth": 0
        }

        total = 0

        for r in rows:
            stats[r["rarity"]] = r["c"]
            total += r["c"]

        # 🏆 топ баланс
        all_users = await conn.fetch("""
            SELECT user_id, diamonds
            FROM users
            ORDER BY diamonds DESC
        """)

        balance_rank = 0
        for i, u in enumerate(all_users, 1):
            if u["user_id"] == msg.from_user.id:
                balance_rank = i
                break

        # 📦 топ коллекция
        col = await conn.fetch("""
            SELECT user_id, SUM(count) as t
            FROM inventory
            GROUP BY user_id
            ORDER BY t DESC
        """)

        collection_rank = 0
        for i, u in enumerate(col, 1):
            if u["user_id"] == msg.from_user.id:
                collection_rank = i
                break

    active = f"{user['active_name']} ❤️ {user['active_hp']}" if user["active_name"] else "Нет"

    await msg.answer(
f"""👤 {user['username']}

💎 {user['diamonds']}

💍 Актив: {active}

📦 Всего: {total}
⚪ {stats['common']} 🟢 {stats['rare']} 🔵 {stats['epic']} 🟣 {stats['legend']} 🟡 {stats['myth']}

🏆 Баланс: #{balance_rank}
📦 Коллекция: #{collection_rank}
"""
    )
