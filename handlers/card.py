from aiogram import Router, F
from aiogram.types import Message
from db import get_user, update_user_time, create_user, cursor, conn
from config import CARD_COOLDOWN
from services.cards import roll_card
from services.cooldown import check_cd
import time

router = Router()

@router.message(F.text.in_(["🎴 Карта", "карта"]))
async def card(msg: Message):
    user = get_user(msg.from_user.id)

    if not user:
        create_user(msg.from_user.id, msg.from_user.username)
        user = get_user(msg.from_user.id)

    last = user[4]

    if not check_cd(last, CARD_COOLDOWN):
        await msg.answer("⏳ Карточку можно раз в 24 часа")
        return

    card_name, rarity = roll_card()

    cursor.execute("""
    INSERT INTO inventory (user_id, card_name, count)
    VALUES (?,?,1)
    ON CONFLICT(user_id, card_name)
    DO UPDATE SET count=count+1
    """, (msg.from_user.id, card_name))

    conn.commit()
    update_user_time(msg.from_user.id, "last_card", int(time.time()))

    await msg.answer(f"🎁 Ты получил:\n\n{card_name}")
