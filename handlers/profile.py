from aiogram import Router, types

router = Router()

@router.message(lambda m: m.text and m.text.lower() in ["профиль","profile","проф","акк"])
async def profile(msg: types.Message):
    await msg.answer("👤 Профиль игрока (заглушка)")
