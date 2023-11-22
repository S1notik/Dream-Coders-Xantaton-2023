from aiogram.enums import ParseMode
from loader import dp, bot
from aiogram import F, types
import sqlite3


@dp.message(F.text == "Пункты сбора♻️")
async def iac(message: types.Message):  # Information about companies
    await message.answer("Про какие пункты сбора вы хотите узнать?")


@dp.message(F.text == "Пункты сбора")
async def iac2(message: types.Message):
    await message.answer("Про какие пункты сбора вы хотите узнать?")


@dp.message(F.text == "ХАНТЫ-МАНСИЙСК🌁")
async def xmao(message: types.Message):
    # con = sqlite3.connect("data/database/")
    # Создание курсора
    cur = con.cursor()
    # Выполнение запроса и получение всех результатов
    # result = cur.execute("""SELECT address FROM info WHERE id = Ханты-Мансийск""")
    con.commit()
    con.close()
    await bot.send_location(message.from_user.id, 61.003895, 69.051789)
    await message.answer(f"<ins>Адресс:</ins> г. Ханты-Мансийск {result}\n"
                         "<ins>Ежедневно:</ins> 10:00 - 20:00\n"
                         "<ins>Обед</ins>: 14:00 - 15:00\n"
                         "<ins>Тех. перерывы</ins>: 11:45 - 12:00 / 16:45 - 17:00<ins>\n",
                         parse_mode=ParseMode.HTML
                         )


@dp.message(F.text == "Ханты-Мансийск")
async def xmao(message: types.Message):
    await bot.send_location(message.from_user.id, 61.003895, 69.051789)
    await message.answer("<ins>Адресс:</ins> г. Ханты-Мансийск ул. Чехова, д. 74\n"
                         "<ins>Ежедневно:</ins> 10:00 - 20:00\n"
                         "<ins>Обед</ins>: 14:00 - 15:00\n"
                         "<ins>Тех. перерывы</ins>: 11:45 - 12:00 / 16:45 - 17:00<ins>\n",
                         parse_mode=ParseMode.HTML
                         )