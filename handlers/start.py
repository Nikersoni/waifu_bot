from aiogram import Router, types
from aiogram.filters import CommandStart
from keyboards.main_menu import main_menu
from db import get_or_create_user

router = Router()


# ✅ ТОЛЬКО /start
@router.message(CommandStart())
async def start(msg: types.Message):

    await get_or_create_user(
        msg.from_user.id,
        msg.from_user.username or "unknown"
    )

    text = (
        "👋 Добро пожаловать в Waifu World!\n\n"
        "🎴 Собирай вайфу и прокачивай коллекцию\n\n"
        "👇 Используй кнопки ниже"
    )

    await msg.answer(text, reply_markup=main_menu())
