from aiogram import Router, types
from keyboards.main_menu import main_menu

router = Router()

@router.message(lambda m: m.chat.type == "private")
async def start(msg: types.Message):
    text = (
        "👋 Добро пожаловать в Waifu World!\n\n"
        "🎴 Собирай вайфу, открывай карточки и развивай коллекцию\n\n"
        "👉 Нажми кнопку ниже или напиши 'карта'"
    )

    await msg.answer(text, reply_markup=main_menu())
