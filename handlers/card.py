from aiogram import Router, F
from aiogram.types import Message
import time

from db import cursor, conn, get_user, create_user, update_user_time
from services.cards import roll_card
from services.cooldown import check_cd
from config import CARD_COOLDOWN

router = Router()

RARITY_EMOJI = {
    "common": "⚪",
    "rare": "🟢",
    "epic": "🔵",
    "legend": "🟣",
    "myth": "🟡"
}

RARITY_NAME = {
    "common": "Обычная",
    "rare": "Редкая",
    "epic": "Эпическая",
    "legend": "Легендарная",
    "myth": "Мифическая"
}


@router.message(F.text.in_(["карта", "🎴 Карта"]))
async def card(msg: Message):

    user = get_user(msg.from_user.id)

    if not user:
        create_user(msg.from_user.id, msg.from_user.username)
        user = get_user(msg.from_user.id)

    # ⏳ КД
    if not check_cd(user[4], CARD_COOLDOWN):
        await msg.answer("⏳ Карточка доступна раз в 24 часа")
        return

    # 🎴 выпадение
    card_name, rarity = roll_card()

    # 📦 в инвентарь
    cursor.execute("""
    INSERT INTO inventory (user_id, card_name, rarity, count)
    VALUES (?,?,?,1)
    ON CONFLICT(user_id, card_name)
    DO UPDATE SET count = count + 1
    """, (msg.from_user.id, card_name, rarity))

    # 💍 делаем активной вайфу
    cursor.execute("""
    UPDATE users
    SET active_name=?,
        active_rarity=?,
        active_level=1,
        active_hp=100
    WHERE user_id=?
    """, (card_name, rarity, msg.from_user.id))

    conn.commit()

    update_user_time(msg.from_user.id, "last_card", int(time.time()))

    # ✨ вывод
    await msg.answer(
f"""✨ ТЕБЕ ВЫПАЛА ВАЙФУ!

{RARITY_EMOJI[rarity]} {card_name}  [{RARITY_NAME[rarity]}]"""
    )
