from aiogram.enums import ParseMode
from loader import dp, bot
from aiogram import F, types
import sqlite3
from keyboards.defoult import towns_keyboard


@dp.message(F.text == "Пункты сбора♻️")
async def iac(message: types.Message):  # Information about companies
    await message.answer("Про какие пункты сбора вы хотите узнать?", reply_markup=towns_keyboard)


@dp.message(F.text == "Пункты сбора")  # 2-ой вариант ввода пользоватиеля
async def iac2(message: types.Message):
    await message.answer("Про какие пункты сбора вы хотите узнать?", reply_markup=towns_keyboard)


@dp.message(F.text == "ХАНТЫ-МАНСИЙСК🌁")
async def xma(message: types.Message):
    con = sqlite3.connect("data/database/information_about_companies")
    # Создание курсора
    cur = con.cursor()
    # Выполнение запроса и получение всех результатов
    result = cur.execute("""SELECT address, time_work, dinner, TechBreak FROM info WHERE name_city = ?""", ('Ханты-Мансийск', ))
    count_table_2 = ""
    count_table_3 = ""
    count_table_4 = ""
    count_table_5 = ""
    for row in result:
        count_table_2 = row[0]
        count_table_3 = row[1]
        count_table_4 = row[2]
        count_table_5 = row[3]
    con.commit()
    con.close()

    await bot.send_location(message.from_user.id, 61.003895, 69.051789)
    await message.answer(f"<ins>Адресс:</ins> г. Ханты-Мансийск, {count_table_2}\n"
                         f"<ins>Ежедневно:</ins> {count_table_3}\n"
                         f"<ins>Обед:</ins> {count_table_4}\n"
                         f"<ins>Тех. перерывы:</ins> {count_table_5}\n",
                         parse_mode=ParseMode.HTML, reply_markup=towns_keyboard
                         )


@dp.message(F.text == "Ханты-Мансийск")  # 2-ой вариант ввода пользоватиеля
async def xma1(message: types.Message):
    con = sqlite3.connect("data/database/information_about_companies")
    # Создание курсора
    cur = con.cursor()
    # Выполнение запроса и получение всех результатов
    result = cur.execute("""SELECT address, time_work, dinner, TechBreak FROM info WHERE name_city = ?""",
                         ('Ханты-Мансийск',))
    count_table_2 = ""
    count_table_3 = ""
    count_table_4 = ""
    count_table_5 = ""
    for row in result:
        count_table_2 = row[0]
        count_table_3 = row[1]
        count_table_4 = row[2]
        count_table_5 = row[3]
    con.commit()
    con.close()

    await bot.send_location(message.from_user.id, 61.003895, 69.051789)
    await message.answer(f"<ins>Адресс:</ins> г. Ханты-Мансийск, {count_table_2}\n"
                         f"<ins>Ежедневно:</ins> {count_table_3}\n"
                         f"<ins>Обед:</ins> {count_table_4}\n"
                         f"<ins>Тех. перерывы:</ins> {count_table_5}\n",
                         parse_mode=ParseMode.HTML, reply_markup=towns_keyboard
                         )


@dp.message(F.text == "СУРГУТ🌁")
async def surg(message: types.Message):
    con = sqlite3.connect("data/database/information_about_companies")
    # Создание курсора
    cur = con.cursor()
    # Выполнение запроса и получение всех результатов
    result = cur.execute("""SELECT address, time_work, dinner, TechBreak FROM info WHERE name_city = ?""", ('Сургут', ))
    count_table_2 = ""
    count_table_3 = ""
    count_table_4 = ""
    count_table_5 = ""
    for row in result:
        count_table_2 = row[0]
        count_table_3 = row[1]
        count_table_4 = row[2]
        count_table_5 = row[3]
    con.commit()
    con.close()

    await bot.send_location(message.from_user.id, 61.257621474483486, 73.45676568947817)
    await message.answer(f"<ins>Адресс:</ins> г. Сургут, {count_table_2}\n"
                         f"<ins>Ежедневно:</ins> {count_table_3}\n"
                         f"<ins>Обед:</ins> {count_table_4}\n"
                         f"<ins>Тех. перерывы:</ins> {count_table_5}\n",
                         parse_mode=ParseMode.HTML, reply_markup=towns_keyboard
                         )


@dp.message(F.text == "Сургут")  # 2-ой вариант ввода пользоватиеля
async def surg1(message: types.Message):
    con = sqlite3.connect("data/database/information_about_companies")
    # Создание курсора
    cur = con.cursor()
    # Выполнение запроса и получение всех результатов
    result = cur.execute("""SELECT address, time_work, dinner, TechBreak FROM info WHERE name_city = ?""", ('Сургут', ))
    count_table_2 = ""
    count_table_3 = ""
    count_table_4 = ""
    count_table_5 = ""
    for row in result:
        count_table_2 = row[0]
        count_table_3 = row[1]
        count_table_4 = row[2]
        count_table_5 = row[3]
    con.commit()
    con.close()

    await bot.send_location(message.from_user.id, 61.257621474483486, 73.45676568947817)
    await message.answer(f"<ins>Адресс:</ins> г. Сургут, {count_table_2}\n"
                         f"<ins>Ежедневно:</ins> {count_table_3}\n"
                         f"<ins>Обед:</ins> {count_table_4}\n"
                         f"<ins>Тех. перерывы:</ins> {count_table_5}\n",
                         parse_mode=ParseMode.HTML, reply_markup=towns_keyboard
                         )


@dp.message(F.text == "НИЖНЕВАРТОВСК🌁")
async def vart(message: types.Message):
    con = sqlite3.connect("data/database/information_about_companies")
    # Создание курсора
    cur = con.cursor()
    # Выполнение запроса и получение всех результатов
    result = cur.execute("""SELECT address, time_work, dinner, TechBreak FROM info WHERE name_city = ?""", ('Нижневартовск', ))
    count_table_2 = ""
    count_table_3 = ""
    count_table_4 = ""
    count_table_5 = ""
    for row in result:
        count_table_2 = row[0]
        count_table_3 = row[1]
        count_table_4 = row[2]
        count_table_5 = row[3]
    con.commit()
    con.close()

    await bot.send_location(message.from_user.id, 60.945131, 76.574973)
    await message.answer(f"<ins>Адресс:</ins> г. Нижневартовск, {count_table_2}\n"
                         f"<ins>Ежедневно:</ins> {count_table_3}\n"
                         f"<ins>Обед:</ins> {count_table_4}\n"
                         f"<ins>Тех. перерывы:</ins> {count_table_5}\n",
                         parse_mode=ParseMode.HTML, reply_markup=towns_keyboard
                         )


@dp.message(F.text == "Нижневартовск")  # 2-ой вариант ввода пользоватиеля
async def vart1(message: types.Message):
    con = sqlite3.connect("data/database/information_about_companies")
    # Создание курсора
    cur = con.cursor()
    # Выполнение запроса и получение всех результатов
    result = cur.execute("""SELECT address, time_work, dinner, TechBreak FROM info WHERE name_city = ?""", ('Нижневартовск', ))
    count_table_2 = ""
    count_table_3 = ""
    count_table_4 = ""
    count_table_5 = ""
    for row in result:
        count_table_2 = row[0]
        count_table_3 = row[1]
        count_table_4 = row[2]
        count_table_5 = row[3]
    con.commit()
    con.close()

    await bot.send_location(message.from_user.id, 60.945131, 76.574973)
    await message.answer(f"<ins>Адресс:</ins> г. Нижневартовск, {count_table_2}\n"
                         f"<ins>Ежедневно:</ins> {count_table_3}\n"
                         f"<ins>Обед:</ins> {count_table_4}\n"
                         f"<ins>Тех. перерывы:</ins> {count_table_5}\n",
                         parse_mode=ParseMode.HTML, reply_markup=towns_keyboard
                         )