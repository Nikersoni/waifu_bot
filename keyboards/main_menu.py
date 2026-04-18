from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🎴 Карты"),
                KeyboardButton(text="👤 Профиль")
            ],
            [
                KeyboardButton(text="🎒 Инвентарь"),
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
