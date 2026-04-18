from aiogram import Router, types

router = Router()

@router.message(lambda m: m.text and m.text.lower() in ["бонус","daily","ежедневка"])
async def bonus(msg: types.Message):
    await msg.answer("🎁 Бонус (заглушка)")
