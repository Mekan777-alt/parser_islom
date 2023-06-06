from config import dp, db_link
import logging
from aiogram import executor
import hendlers
import sqlite3


def create_table():
    """Create table if not exists."""

    conn = sqlite3.connect(db_link)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ariza_shakli TEXT,
            davlat TEXT,
            shahar TEXT, 
            visametric TEXT, 
            turlari TEXT, 
            soni INT, 
            name TEXT, 
            firstname TEXT,
            full_name TEXT,
            mileti TEXT, 
            birthday INT, 
            month INT, 
            year INT, 
            number_passport TEXT,
            year_passport TEXT, 
            phone_number TEXT, 
            alt_phone TEXT, 
            email TEXT,
            password TEXT
        );
        """
    )
    conn.commit()
    conn.close()


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    create_table()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
