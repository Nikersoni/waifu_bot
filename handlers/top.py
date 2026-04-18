from aiogram import Router, types

router = Router()

@router.message(lambda m: m.text and m.text.lower() in ["топ","top","рейтинг"])
async def top(msg: types.Message):
    await msg.answer("🏆 Топ игроков (заглушка)")
