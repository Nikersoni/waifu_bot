from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from services.user import ensure_user
from handlers.card import card  # используем ту же логику

router = Router()


# 👋 БОТ ДОБАВЛЕН В ГРУППУ
@router.message(F.new_chat_members)
async def on_bot_added(msg: types.Message):

    for user in msg.new_chat_members:
        if user.is_bot:

            keyboard = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="🎴 Получить карту",
                            callback_data="get_card"
                        )
                    ]
                ]
            )

            await msg.answer(
                "✨ Добро пожаловать в Waifu World\n\n"
                "Здесь ты:\n"
                "• собираешь вайфу 🎴\n"
                "• прокачиваешь их ❤️\n"
                "• участвуешь в рейтинге 🏆\n\n"
                "📖 Список команд:\n"
                "карта — получить вайфу\n"
                "профиль — профиль\n"
                "инв — инвентарь\n"
                "бонус — ежедневная награда\n"
                "топ — рейтинг игроков\n"
                "рынок — торговля (скоро)\n\n"
                "👇 Получи свою первую карту",
                reply_markup=keyboard
            )


# 🎴 КНОПКА → ВЫЗОВ КОМАНДЫ КАРТА
@router.callback_query(F.data == "get_card")
async def get_card_callback(call: types.CallbackQuery):

    # создаём пользователя
    await ensure_user(call.message)

    # 👉 вызываем ту же логику, что и команда "карта"
    fake_msg = call.message
    fake_msg.from_user = call.from_user
    fake_msg.text = "карта"

    await card(fake_msg)

    await call.answer()
