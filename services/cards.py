import random

cards = [
    ("Луна", "common"),
    ("Мика", "rare"),
    ("Ая", "epic"),
    ("Хината", "legend"),
    ("Акари", "myth")
]

def roll_card():
    r = random.randint(1, 100)

    if r <= 50:
        pool = [c for c in cards if c[1] == "common"]
    elif r <= 80:
        pool = [c for c in cards if c[1] == "rare"]
    elif r <= 95:
        pool = [c for c in cards if c[1] == "epic"]
    elif r <= 99:
        pool = [c for c in cards if c[1] == "legend"]
    else:
        pool = [c for c in cards if c[1] == "myth"]

    return random.choice(pool)
