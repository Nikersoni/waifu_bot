from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎴 Карта"), KeyboardButton(text="👤 Профиль")],
        [KeyboardButton(text="🎒 Инвентарь"), KeyboardButton(text="🎁 Бонус")],
        [KeyboardButton(text="🏆 Топ")]
    ],
    resize_keyboard=True
)
