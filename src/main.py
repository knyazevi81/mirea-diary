from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv


load_dotenv()
bot = Bot(os.getenv("TG_KEY"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)