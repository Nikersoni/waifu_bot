import random

CARDS = [
    ("Хината", "rare"),
    ("Аянами Рей", "legend"),
    ("Асуна", "epic"),
    ("Мику", "common"),
    ("Zero Two", "epic"),
    ("Rem", "rare"),
    ("Emilia", "rare"),
    ("Kurumi", "legend"),
    ("Nezuko", "epic"),
    ("Hinata", "common"),
]

RARITY_CHANCE = {
    "common": 50,
    "rare": 30,
    "epic": 12,
    "legend": 6,
    "myth": 2
}

EMOJI = {
    "common": "⚪",
    "rare": "🟢",
    "epic": "🔵",
    "legend": "🟣",
    "myth": "🟡"
}

def get_random_card():
    roll = random.randint(1, 100)
    total = 0

    for rarity, chance in RARITY_CHANCE.items():
        total += chance
        if roll <= total:
            pool = [c for c in CARDS if c[1] == rarity]
            return random.choice(pool)

    return random.choice(CARDS)
