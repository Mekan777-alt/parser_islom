from aiogram import Dispatcher, Bot, types
from local_config import TOKEN
import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage


loop = asyncio.get_event_loop()
storage = MemoryStorage()
db_link = 'db.db'

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage, loop=loop)
