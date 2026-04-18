import random

def bonus_amount():
    return random.randint(10, 25)


def sell_value(rarity):
    return {
        "common": 5,
        "rare": 15,
        "epic": 40,
        "legend": 100,
        "myth": 0
    }[rarity]


def dust_value(rarity):
    return {
        "common": 2,
        "rare": 6,
        "epic": 15,
        "legend": 40,
        "myth": 0
    }[rarity]
