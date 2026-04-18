from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text.in_(["🎒 Инвентарь", "инв", "инвентарь"]))
async def inventory(msg: Message):
    await msg.answer("🎒 Инвентарь пока в разработке")
