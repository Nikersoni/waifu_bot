from aiogram import Router, types

router = Router()


@router.message(lambda m: m.text and m.text.lower().strip() in ["инв", "инвентарь", "🎒 инв"])
async def inv(msg: types.Message):
    await msg.answer("🎒 Инвентарь (заглушка)")
