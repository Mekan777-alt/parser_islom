from config import dp
import logging
from aiogram import executor
import hendlers


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
