from aiogram import Router, types

router = Router()


@router.message(lambda m: m.text and m.text.lower().strip() in ["хелп", "help", "❓ хелп"])
async def help_cmd(msg: types.Message):
    await msg.answer(
        "📖 ПОМОЩЬ\n\n"
        "🎴 карта — получить вайфу\n"
        "👤 профиль — информация\n"
        "🎒 инв — инвентарь\n"
        "🎁 бонус — ежедневная награда\n"
        "🏪 рынок — торговля (скоро)\n"
        "🏆 топ — рейтинг игроков\n"
    )
