from aiogram import Router, types

router = Router()


@router.message()
async def debug(msg: types.Message):

    print("GROUP MESSAGE:", msg.text, msg.chat.type)

    if msg.chat.type in ["group", "supergroup"]:
        if msg.text:
            await msg.answer("✅ я вижу сообщение")
