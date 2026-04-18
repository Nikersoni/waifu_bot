async def run_migrations(conn):
    """
    Авто-обновление БД при старте бота
    """

    # 👤 USERS
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            username TEXT,
            created_at TIMESTAMP DEFAULT NOW()
        )
    """)

    # 🎴 INVENTORY
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            user_id BIGINT,
            card_name TEXT,
            rarity TEXT,
            count INT DEFAULT 1,
            PRIMARY KEY (user_id, card_name)
        )
    """)

    # ⏳ COOLDOWNS
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS cooldowns (
            user_id BIGINT PRIMARY KEY,
            last_card TIMESTAMP,
            last_bonus TIMESTAMP
        )
    """)

    print("✅ DB migrations completed")
