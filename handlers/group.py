from aiogram import Router, types

router = Router()


@router.message()
async def test(msg: types.Message):

    print("DEBUG:", msg.text, msg.chat.type)

    await msg.answer("🟢 BOT ALIVE")
