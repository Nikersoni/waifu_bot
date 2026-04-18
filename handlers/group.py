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
     router.message(lambda           "профиль — профиль игрока\n"
                "инв — инвентарь\n"
                "бонус — ежедневная награда\n"
                "топ — рейтинг\n"
                "рынок — торговля\n"
                "хелп — помощь\n\n"
                "🔥 Начните играть прямо сейчас!"
            )

