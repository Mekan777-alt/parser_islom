from config import dp
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from context.context import Users
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands='start')
async def start_cmd(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Schengen Visa')
    await Users.ariza_shakli.set()
    await message.answer('Введите данные поочередности', reply_markup=markup)


@dp.message_handler(state=Users.ariza_shakli)
async def cmd2(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Germany')
    markup.add('Sweden')
    async with state.proxy() as data:
        data['ariza_shakli'] = message.text
        await Users.next()
        await message.answer('Tashrif buyuradigan davlat', reply_markup=markup)


@dp.message_handler(state=Users.tashrif_davlet)
async def cmd3(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Andijan')
    markup.add('Angren')
    markup.add('Bekobod')
    markup.add('Bukhara')
    markup.add('Chirchiq')
    markup.add('Fergana')
    markup.add('Jizzakh')
    markup.add('Kokand')
    markup.add('Margilan')
    markup.add('Namangan')
    markup.add('Navoiy')
    markup.add('Nukus')
    markup.add('Olmaliq')
    markup.add('Qarshi')
    markup.add('Samarkand')
    markup.add('Shahrisabz')
    markup.add('Tashkent')
    markup.add('Termez')
    markup.add('Urgench')
    async with state.proxy() as data:
        data['tashrif_davlet'] = message.text
        await Users.next()
        await message.answer('Istiqomat qiladigan shahar', reply_markup=markup)


@dp.message_handler(state=Users.istiqomat)
async def cmd4(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Tashkent')
    async with state.proxy() as data:
        data['istiqomat'] = message.text
        await Users.next()
        await message.answer('Visametric idorasi', reply_markup=markup)


@dp.message_handler(state=Users.visametric)
async def cmd5(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('NORMAL')
    async with state.proxy() as data:
        data['visametric'] = message.text
        await Users.next()
        await message.answer('Xizmat turlari', reply_markup=markup)


@dp.message_handler(state=Users.xizmat)
async def cmd6(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('1 arizachi')
    async with state.proxy() as data:
        data['xizmat'] = message.text
        await Users.next()
        await message.answer('Ariza beruvchilar soni', reply_markup=markup)


@dp.message_handler(state=Users.ariza)
async def cmd7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ariza'] = message.text
        await message.answer('Отправлено! \n'
                             'Ожидайте')
        print(f"1. {data['ariza_shakli']} \n"
              f"2. {data['tashrif_davlet']}\n"
              f"3. {data['istiqomat']}\n"
              f"4. {data['visametric']}\n"
              f"5. {data['xizmat']}\n"
              f"6. {data['ariza']}\n")
