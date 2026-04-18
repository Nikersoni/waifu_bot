from aiogram import Router, types

router = Router()

@router.message(lambda m: m.text and m.text.lower() in ["хелп","help","команды"])
async def help_cmd(msg: types.Message):
    await msg.answer("📖 Помощь (заглушка)")
