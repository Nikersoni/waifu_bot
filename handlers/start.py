from aiogram import Router, F
from aiogram.types import Message
from db import create_user

router = Router()


@router.message(F.text == "/start")
async def start(msg: Message):

    await create_user(
        msg.from_user.id,
        msg.from_user.username
    )

    await msg.answer("👋 Добро пожаловать в Waifu World")
