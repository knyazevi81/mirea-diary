from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup
from statemachine import ClientState

from src.handlers import main_handler
from src.initmain import dp, bot
from colorama import Fore


async def start_message(_) -> None:
    print(Fore.WHITE + "[" + Fore.GREEN + "INFO" + Fore.WHITE + "] Bot launched successfully!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=start_message)