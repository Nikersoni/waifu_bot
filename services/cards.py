import random

CARDS = [
    ("Луна", "common"),
    ("Мика", "common"),
    ("Сора", "common"),
    ("Рин", "common"),

    ("Аой", "rare"),
    ("Мэй", "rare"),

    ("Ая", "epic"),
    ("Хикари", "epic"),

    ("Хината", "legend"),
    ("Акари", "myth")
]


def roll_card():
    r = random.randint(1, 100)

    if r <= 50:
        pool = [c for c in CARDS if c[1] == "common"]
    elif r <= 80:
        pool = [c for c in CARDS if c[1] == "rare"]
    elif r <= 95:
        pool = [c for c in CARDS if c[1] == "epic"]
    elif r <= 99:
        pool = [c for c in CARDS if c[1] == "legend"]
    else:
        pool = [c for c in CARDS if c[1] == "myth"]

    return random.choice(pool)
