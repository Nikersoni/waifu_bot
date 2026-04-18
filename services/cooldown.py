from datetime import datetime, timedelta

COOLDOWN_HOURS = 24


# 🎴 КАРТА
async def can_get_card(conn, user_id: int):
    row = await conn.fetchrow(
        "SELECT last_card FROM cooldowns WHERE user_id=$1",
        user_id
    )

    if not row or not row["last_card"]:
        return True

    return datetime.utcnow() - row["last_card"] >= timedelta(hours=COOLDOWN_HOURS)


async def update_card_cd(conn, user_id: int):
    await conn.execute("""
        INSERT INTO cooldowns (user_id, last_card)
        VALUES ($1, NOW())
        ON CONFLICT (user_id)
        DO UPDATE SET last_card = NOW()
    """, user_id)


# 🎁 БОНУС
async def can_get_bonus(conn, user_id: int):
    row = await conn.fetchrow(
        "SELECT last_bonus FROM cooldowns WHERE user_id=$1",
        user_id
    )

    if not row or not row["last_bonus"]:
        return True

    return datetime.utcnow() - row["last_bonus"] >= timedelta(hours=COOLDOWN_HOURS)


async def update_bonus_cd(conn, user_id: int):
    await conn.execute("""
        INSERT INTO cooldowns (user_id, last_bonus)
        VALUES ($1, NOW())
        ON CONFLICT (user_id)
        DO UPDATE SET last_bonus = NOW()
    """, user_id)
