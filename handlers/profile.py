from aiogram import Router, types

router = Router()


@router.message(lambda m: m.text and m.text.lower().strip() in ["профиль", "👤 профиль"])
async def profile(msg: types.Message):
    await msg.answer("👤 Профиль (заглушка)")
