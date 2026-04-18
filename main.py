import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from db import init_db

# handlers
from handlers import start, card, profile, inventory, bonus, top, institute

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# регистрация роутеров
dp.include_router(start.router)
dp.include_router(card.router)
dp.include_router(profile.router)
dp.include_router(inventory.router)
dp.include_router(bonus.router)
dp.include_router(top.router)
dp.include_router(institute.router)


async def main():
    # 🟢 инициализация PostgreSQL + таблиц
    await init_db()

    print("🚀 Bot started successfully")

    # запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
