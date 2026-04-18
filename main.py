import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from db import init_db

from handlers import start, card, profile, inventory, bonus, top, institute

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(card.router)
dp.include_router(profile.router)
dp.include_router(inventory.router)
dp.include_router(bonus.router)
dp.include_router(top.router)
dp.include_router(institute.router)


async def main():
    init_db()
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
