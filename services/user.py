from db import get_or_create_user


async def ensure_user(msg):
    await get_or_create_user(
        msg.from_user.id,
        msg.from_user.username or "unknown"
    )
