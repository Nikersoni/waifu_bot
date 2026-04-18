from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🎴 Карта"),
                KeyboardButton(text="👤 Профиль")
            ],
            [
                KeyboardButton(text="🎒 Инв"),
                KeyboardButton(text="🏪 Рынок")
            ],
            [
                KeyboardButton(text="🎁 Бонус"),
                KeyboardButton(text="🏆 Топ")
            ],
            [
                KeyboardButton(text="🏫 Институт"),
                KeyboardButton(text="❓ Хелп")
            ]
        ],
        resize_keyboard=True
    )
