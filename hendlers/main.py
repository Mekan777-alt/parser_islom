from config import dp, db_link
import sqlite3
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
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
    markup = ReplyKeyboardRemove()
    async with state.proxy() as data:
        data['ariza'] = message.text
        await Users.next()
        await message.answer('Имя', reply_markup=markup)


@dp.message_handler(state=Users.name)
async def cmd8(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await Users.next()
        await message.answer('Фамилия')


@dp.message_handler(state=Users.firstname)
async def cmd9(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['firstname'] = message.text
        await Users.next()
        await message.answer('Полное имя')


@dp.message_handler(state=Users.full_name)
async def cmd10(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['full_name'] = message.text
        await Users.next()
        await message.answer('Национальность')


@dp.message_handler(state=Users.mileti)
async def cmd11(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mileti'] = message.text
        await Users.next()
        await message.answer('Дата рождения (в цифрах)')


@dp.message_handler(state=Users.birthday)
async def cmd12(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['birthday'] = message.text
        await Users.next()
        await message.answer('Месяц рождения (в цифрах)')


@dp.message_handler(state=Users.month)
async def cmd13(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['month'] = message.text
        await Users.next()
        await message.answer('Год рождения (в цифрах)')


@dp.message_handler(state=Users.year)
async def cmd14(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['year'] = message.text
        await Users.next()
        await message.answer('Номер пасспорта')


@dp.message_handler(state=Users.number_passport)
async def cmd15(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_passport'] = message.text
        await Users.next()
        await message.answer('Срок пасспорта (день.месяц.год) в цифрах через точку')


@dp.message_handler(state=Users.year_passport)
async def cmd16(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['year_passport'] = message.text
        await Users.next()
        await message.answer('Телефон номер')


@dp.message_handler(state=Users.phone_number)
async def cmd17(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
        await Users.next()
        await message.answer('Альтернативный номер телефона')


@dp.message_handler(state=Users.alt_phone)
async def cmd18(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['alt_phone'] = message.text
        await Users.next()
        await message.answer('Почта')


@dp.message_handler(state=Users.email)
async def cmd19(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
        await Users.next()
        await message.answer('Пароль')


@dp.message_handler(state=Users.password)
async def cmd20(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Верно')
    async with state.proxy() as data:
        data['password'] = message.text
        await Users.next()
        await message.answer(f"1. {data['ariza_shakli']}\n"
                             f"2. {data['tashrif_davlet']}\n"
                             f"3. {data['istiqomat']}\n"
                             f"4. {data['visametric']}\n"
                             f"5. {data['xizmat']}\n"
                             f"6. {data['ariza']}\n"
                             f"7. {data['name']}\n"
                             f"8. {data['firstname']}\n"
                             f"9. {data['full_name']}\n"
                             f"10. {data['mileti']}\n"
                             f"11. {data['birthday']}.{data['month']}.{data['year']}\n"
                             f"12. {data['number_passport']}\n"
                             f"13. {data['year_passport']}\n"
                             f"14. {data['phone_number']}\n"
                             f"15. {data['alt_phone']}\n"
                             f"16. {data['email']}\n"
                             f"17. {data['password']}", reply_markup=markup)


@dp.message_handler(text='Верно')
async def done(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        conn = sqlite3.connect(db_link)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users(visa, ariza_shakli, davlat, shahar, visametric, "
                       "turlari, soni, name, firstname, mileti, birthday, month, year, number_passport, "
                       "year_passport, phone_number, alt_phone, email, password) "
                       "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (data['ariza_shakli'], data['tashrif_davlet'], data['istiqomat'], data['visametric'],
                        data['xizmat'],
                        data['ariza'], data['name'], data['firstname'], data['full_name'],
                        data['mileti'], data['birthday'], data['month'], data['year'], data['number_passport'],
                        data['year_passport'],
                        data['phone_number'], data['alt_phone'], data['email'], data['password'],))
        conn.commit()
        conn.close()
        await message.answer('Принято')
