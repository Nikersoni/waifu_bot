import random

from services.inventory import add_card_db


# 🎴 ВСЕ КАРТЫ (25 ШТУК)

COMMON_CARDS = [
    ("Мику Нормал", "common"),
    ("Хината Коноха", "common"),
    ("Сакура Харуна", "common"),
    ("Нана Обычная", "common"),
    ("Юи Школьница", "common"),
    ("Мэй Тихая", "common"),
    ("Алиса Новичок", "common"),
    ("Рин Соло", "common"),
]

RARE_CARDS = [
    ("Хината Тренированная", "rare"),
    ("Рем Служанка", "rare"),
    ("Эмилия Маг", "rare"),
    ("Асуна Рыцарь", "rare"),
    ("Мику Концерт", "rare"),
    ("Незуко Усиленная", "rare"),
    ("Кагуя Умная", "rare"),
]

EPIC_CARDS = [
    ("Zero Two Пилот", "epic"),
    ("Асуна Легендарный Меч", "epic"),
    ("Незуко Демон Форма", "epic"),
    ("Рем Боевая", "epic"),
    ("Эмилия Ледяная Магия", "epic"),
]

LEGEND_CARDS = [
    ("Куруми Времени", "legend"),
    ("Zero Two Королева Кода", "legend"),
    ("Мику Голограмма", "legend"),
]

MYTH_CARDS = [
    ("Аянами Рей Пустота", "myth"),
]


CARDS = (
    COMMON_CARDS +
    RARE_CARDS +
    EPIC_CARDS +
    LEGEND_CARDS +
    MYTH_CARDS
)


# 🎲 БАЛАНС ШАНСОВ
RARITY_CHANCE = [
    ("common", 65),
    ("rare", 25),
    ("epic", 8),
    ("legend", 1),
    ("myth", 1),
]


# 🎨 ЭМОДЗИ РЕДКОСТЕЙ
EMOJI = {
    "common": "⚪",
    "rare": "🟢",
    "epic": "🔵",
    "legend": "🟣",
    "myth": "🟡"
}


# 🎲 ВЫБОР РЕДКОСТИ
def roll_rarity():
    roll = random.randint(1, 100)
    current = 0

    for rarity, chance in RARITY_CHANCE:
        current += chance
        if roll <= current:
            return rarity

    return "common"


# 🎴 ВЫБОР КАРТЫ
def get_card():
    rarity = roll_rarity()

    pool = [c for c in CARDS if c[1] == rarity]

    if not pool:
        pool = CARDS

    return random.choice(pool)


# 🧾 ФОРМАТ ВЫВОДА
def format_card(card):
    name, rarity = card
    return f"{EMOJI.get(rarity,'')} {name} [{rarity.upper()}]"


# 🚀 ОСНОВНАЯ ФУНКЦИЯ (ДЛЯ БОТА)
async def give_card(pool, user_id: int):

    card = get_card()
    name, rarity = card

    # 💾 сохраняем в БД
    await add_card_db(pool, user_id, name, rarity)

    return f"🎴 ТЫ ПОЛУЧИЛ:\n\n{format_card(card)}"
