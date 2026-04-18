from aiogram import Router, types, F

from services.user import ensure_user
from services.cards import give_card

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
                "рынок — торговля\n"
                "хелп — помощь\n\n"
                "🔥 Просто пиши команды в чат"
            )


# 💬 ОБРАБОТКА КОМАНД В ГРУППЕ (REPLY MODE)
@router.message(lambda m: m.chat.type in ["group", "supergroup"])
async def group_router(msg: types.Message):

    if not msg.text:
        return

    text = msg.text.lower().strip()

    # 👤 регистрируем пользователя всегда
    await ensure_user(msg)

    # 🎴 КАРТА
    if text in ["карта", "🎴 карта"]:
        result = await give_card(msg.from_user.id)

        await msg.answer(
            result,
            reply_to_message_id=msg.message_id
        )

    # 👤 ПРОФИЛЬ
    elif text in ["профиль", "👤 профиль"]:
        await msg.answer(
            "👤 Профиль игрока",
            reply_to_message_id=msg.message_id
        )

    # 🎒 ИНВЕНТАРЬ
    elif text in ["инв", "инвентарь", "🎒 инв"]:
        await msg.answer(
            "🎒 Инвентарь",
            reply_to_message_id=msg.message_id
        )

    # 🎁 БОНУС
    elif text in ["бонус", "🎁 бонус"]:
        await msg.answer(
            "🎁 Ежедневная награда получена",
            reply_to_message_id=msg.message_id
        )

    # 🏆 ТОП
    elif text in ["топ", "🏆 топ"]:
        await msg.answer(
            "🏆 Топ игроков",
            reply_to_message_id=msg.message_id
        )

    # 🏪 РЫНОК
    elif text in ["рынок", "🏪 рынок"]:
        await msg.answer(
            "🏪 Рынок в разработке",
            reply_to_message_id=msg.message_id
        )

    # ❓ ХЕЛП
    elif text in ["хелп", "help", "❓ хелп"]:
        await msg.answer(
            "📖 Команды:\n"
            "карта\n"
            "профиль\n"
            "инв\n"
            "бонус\n"
            "топ\n"
            "рынок",
            reply_to_message_id=msg.message_id
        )
