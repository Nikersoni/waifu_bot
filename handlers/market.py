from aiogram import Router, types

router = Router()


@router.message(lambda m: m.text and m.text.lower().strip() in ["рынок", "🏪 рынок"])
async def market(msg: types.Message):
    await msg.answer(
        "🏪 РЫНОК В РАЗРАБОТКЕ\n\n"
        "💠 Скоро здесь можно будет:\n"
        "• продавать вайфу\n"
        "• покупать карточки\n"
        "• обменивать пыль\n"
    )
