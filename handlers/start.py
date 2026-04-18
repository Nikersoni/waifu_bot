from aiogram import Router, types
from keyboards.main_menu import main_menu
from db import get_or_create_user

router = Router()


@router.message(lambda m: m.chat.type == "private")
async def start(msg: types.Message):

    # 🧠 создаём пользователя в БД
    await get_or_create_user(
        msg.from_user.id,
        msg.from_user.username or "unknown"
    )

    text = (
        "👋 Добро пожаловать в Waifu World!\n\n"
        "🎴 Открывай карточки, собирай коллекцию и прокачивайся\n\n"
        "👉 Нажми кнопку ниже или напиши 'карта'"
    )

    await msg.answer(text, reply_markup=main_menu())
