from aiogram import Router, types

router = Router()


@router.message(lambda m: m.text and m.text.lower().strip() in ["карта", "🎴 карта"])
async def card(msg: types.Message):
    await msg.answer("🎴 Ты открыл карту (заглушка)")
