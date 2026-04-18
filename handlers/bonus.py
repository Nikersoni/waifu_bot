from aiogram import Router, types

router = Router()


@router.message(lambda m: m.text and m.text.lower().strip() in ["бонус", "🎁 бонус"])
async def bonus(msg: types.Message):
    await msg.answer("🚧 Бонус в разработке")
