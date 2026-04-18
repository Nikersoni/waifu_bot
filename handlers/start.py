from aiogram import Router, F
from aiogram.types import Message
from db import create_user

from keyboards.reply import main_kb

router = Router()

@router.message(F.text == "/start")
async def start(msg: Message):

    create_user(msg.from_user.id, msg.from_user.username)

    await msg.answer(
f"""👋 Привет, {msg.from_user.username}

🎴 Добро пожаловать в Waifu Cards

━━━━━━━━━━━━━━━
Собирай карточки, продавай дубликаты,
развивай свою коллекцию

🎁 Получай бонусы каждый день
🎴 Открывай карточки раз в 24 часа

━━━━━━━━━━━━━━━
Нажми кнопку ниже:""",
    reply_markup=main_kb
    )
