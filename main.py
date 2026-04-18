import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from db import init_db

# handlers
from handlers import start
from handlers import card
from handlers import profile
from handlers import inventory
from handlers import bonus
from handlers import top
from handlers import institute


# логирование (важно для хостинга)
logging.basicConfig(level=logging.INFO)

# bot + dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# подключение роутеров
dp.include_router(start.router)
dp.include_router(card.router)
dp.include_router(profile.router)
dp.include_router(inventory.router)
dp.include_router(bonus.router)
dp.include_router(top.router)
dp.include_router(institute.router)


async def main():
    # инициализация базы
    init_db()

    print("🤖 Bot started...")

    # запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
