from aiogram import types, Dispatcher
from src.initmain import bot


async def mainhandler(message: types.message) -> None:
    await bot.send_message(
        message.from_user.id,
        "hello"
    )


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(mainhandler)