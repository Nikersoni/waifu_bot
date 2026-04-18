from aiogram import Router, types

router = Router()


@router.message(lambda m: m.text and m.text.lower().strip() in ["инв", "инвентарь", "🎒 инвентарь"])
async def inv(msg: types.Message):
    await msg.answer("🚧 инвентарь в разработке")
