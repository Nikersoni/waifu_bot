from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text.in_(["🏫 Институт", "институт"]))
async def inst(msg: Message):
    await msg.answer("🚧 Институт в разработке")
