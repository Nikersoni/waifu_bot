from aiogram import Router, types, F

from services.user import ensure_user
from handlers.card import card

router = Router()


# 👋 Приветствие при добавлении бота в группу
@router.message(F.new_chat_members)
async def on_bot_added(msg: types.Message):

    for user in msg.new_chat_members:
        if user.is_bot:

            await msg.answer(
                "✨ Добро пожаловать в Waifu World\n\n"
                "Здесь ты:\n"
                "• собираешь вайфу 🎴\n"
                "• прокачиваешь их ❤️\n"
                "• участвуешь в рейтинге 🏆\n\n"
                "📖 Список команд:\n"
                "карта — получить вайфу\n"
                "профиль — профиль игрока\n"
                "инв — инвентарь\n"
                "бонус — ежедневная награда\n"
                "топ — рейтинг игроков\n"
                "рынок — торговля (скоро)\n"
                "хелп — помощь\n\n"
                "🔥 Просто пиши команды в чат"
            )


# 🎴 обычные сообщения в группе → обрабатываем как ЛС
@router.message(lambda m: m.chat.type in ["group", "supergroup"])
async def group_router(msg: types.Message):

    if not msg.text:
        return

    text = msg.text.lower().strip()

    # 👤 регистрируем пользователя
    await ensure_user(msg)

    # 🎴 карта
    if text in ["карта", "🎴 карта"]:
        await card(msg)

    # дальше можно добавлять аналогично:
    elif text in ["профиль", "👤 профиль"]:
        await msg.answer("👤 Профиль игрока")

    elif text in ["инв", "инвентарь", "🎒 инв"]:
        await msg.answer("🎒 Инвентарь")

    elif text in ["бонус", "🎁 бонус"]:
        await msg.answer("🎁 Бонус получен")

    elif text in ["топ", "🏆 топ"]:
        await msg.answer("🏆 Топ игроков")

    elif text in ["рынок", "🏪 рынок"]:
        await msg.answer("🏪 Рынок в разработке")

    elif text in ["хелп", "help", "❓ хелп"]:
        await msg.answer(
            "📖 Команды:\n"
            "карта\n"
            "профиль\n"
            "инв\n"
            "бонус\n"
            "топ\n"
            "рынок"
        )
