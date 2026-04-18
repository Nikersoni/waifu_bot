from aiogram import Router, types

router = Router()


# 👋 бот добавлен в группу
@router.message(lambda m: m.new_chat_members)
async def on_bot_added(msg: types.Message):

    for user in msg.new_chat_members:
        if user.is_bot:

            await msg.answer(
                "👋 Спасибо за добавление меня в группу!\n\n"
                "🎴 WAIFU WORLD БОТ\n\n"
                "📖 Команды:\n"
                "карта — получить вайфу\n"
                "профиль — профиль игрока\n"
                "инв — инвентарь\n"
                "бонус — ежедневная награда\n"
                "топ — рейтинг\n"
                "рынок — торговля\n"
                "хелп — помощь\n\n"
                "🔥 Начните играть прямо сейчас!"
            )


# 💬 команды в группе
@router.message(lambda m: m.chat.type in ["group", "supergroup"])
async def group_commands(msg: types.Message):

    text = msg.text.lower().strip()

    if text in ["карта", "карта🎴", "🎴 карта"]:
        await msg.answer("🎴 Группа: ты получил вайфу!")

    elif text in ["профиль", "👤 профиль"]:
        await msg.answer("👤 Группа профиль (заглушка)")

    elif text in ["инв", "инвентарь", "🎒 инв"]:
        await msg.answer("🎒 Групповой инвентарь (заглушка)")

    elif text in ["бонус", "🎁 бонус"]:
        await msg.answer("🎁 Групповой бонус (заглушка)")

    elif text in ["топ", "🏆 топ"]:
        await msg.answer("🏆 Групповой топ (заглушка)")

    elif text in ["рынок", "🏪 рынок"]:
        await msg.answer("🏪 Рынок в группе (скоро)")

    elif text in ["хелп", "help", "❓ хелп"]:
        await msg.answer(
            "📖 Команды группы:\n"
            "карта, профиль, инв, бонус, топ, рынок, хелп"
                  )
