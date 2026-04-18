from aiogram import Router, types

router = Router()

@router.message(lambda m: m.text and m.text.lower() in ["карта","card","ролл","крутка"])
async def card(msg: types.Message):
    await msg.answer("✨ Ты крутишь гачу...\n🎴 (логика выпадения позже)")
