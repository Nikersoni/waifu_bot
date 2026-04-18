from aiogram import Router, types

router = Router()


@router.message(lambda m: m.text and m.text.lower().strip() in ["карта", "🎴 карты"])
async def card(msg: types.Message):
    await msg.answer("🚧 карты в разработке")
