from aiogram import Dispatcher, Bot, types
from local_config import TOKEN
import asyncio


loop = asyncio.get_event_loop()
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, loop=loop)
