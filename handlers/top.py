from aiogram import Router, types

router = Router()


@router.message(lambda m: m.text and m.text.lower().strip() in ["топ", "🏆 топ"])
async def top(msg: types.Message):
    await msg.answer("🚧 топ в разработке")
    
@router.message()
async def test(msg: types.Message):
    print("LS:", msg.text)
