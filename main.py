import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from db import init_db

from handlers import (
    start,
    card,
    profile,
    inventory,
    bonus,
    top,
    market,
    help,
    group,
    institute
)


# 📌 логирование
logging.basicConfig(level=logging.INFO)


async def main():

    # 🤖 бот создаём СРАЗУ
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # 🗄️ БД + pool
    pool = await init_db()

    # 💾 сохраняем pool в bot (ВАЖНО)
    bot["db_pool"] = pool

    # 📦 роутеры
    dp.include_router(group.router)
    dp.include_router(start.router)
    dp.include_router(card.router)
    dp.include_router(profile.router)
    dp.include_router(inventory.router)
    dp.include_router(bonus.router)
    dp.include_router(top.router)
    dp.include_router(market.router)
    dp.include_router(help.router)
    dp.include_router(institute.router)

    print("🚀 BOT STARTED")

    # 🤖 запуск
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
