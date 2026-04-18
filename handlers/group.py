from aiogram import Router, types

router = Router()


@router.message()
async def group_router(msg: types.Message):

    print("GROUP MESSAGE:", msg.text, msg.chat.type)

    if msg.chat.type not in ["group", "supergroup"]:
        return

    if not msg.text:
        return

    text = msg.text.lower().strip()

    try:

        # 🧪 тест ответа
        if text == "карта":
            await msg.answer("🎴 тест карта", reply_to_message_id=msg.message_id)

        elif text == "топ":
            await msg.answer("🏆 тест топ", reply_to_message_id=msg.message_id)

        else:
            await msg.answer("✅ вижу сообщение", reply_to_message_id=msg.message_id)

    except Exception as e:
        print("❌ ERROR IN GROUP:", e)
