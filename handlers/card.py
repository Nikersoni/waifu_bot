from aiogram import Router, types
from services.user import ensure_user
from services.cards import give_card

router = Router()


# 🎴 ТЕКСТОВАЯ КОМАНДА (ЛС + ГРУППА)
@router.message(lambda m: m.text and m.text.lower().strip() in ["карта", "🎴 карта"])
async def card(msg: types.Message):

    # 👤 регистрируем пользователя
    await ensure_user(msg)

    # 🎴 выдача карты (единая логика)
    result = await give_card(msg.from_user.id)

    await msg.answer(result)
