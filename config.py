from aiogram import Dispatcher, Bot, types
from local_config import TOKEN
import asyncio
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.data import Database

path = os.getcwd() + "/data/data.db"


loop = asyncio.get_event_loop()
storage = MemoryStorage()

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage, loop=loop)
db = Database(path)
