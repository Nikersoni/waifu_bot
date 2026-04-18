async def add_card_db(pool, user_id: int, card_name: str, rarity: str):

    async with pool.acquire() as conn:

        await conn.execute("""
            INSERT INTO inventory (user_id, card_name, rarity, count)
            VALUES ($1, $2, $3, 1)
            ON CONFLICT (user_id, card_name)
            DO UPDATE SET count = inventory.count + 1
        """, user_id, card_name, rarity)
