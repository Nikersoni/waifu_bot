from aiogram import Router, types

router = Router()

@router.message(lambda m: m.text and m.text.lower() in ["инв","инвентарь","inventory","коллекция"])
async def inv(msg: types.Message):
    await msg.answer("🎒 Инвентарь (заглушка)")
