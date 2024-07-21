from aiogram.filters import CommandStart
from loader import dp
from keyboards.defoult.reply_buttons import start_keyboard
from aiogram import types, F
import sqlite3


@dp.message(CommandStart())
async def start(message: types.Message):
    # con = sqlite3.connect("data/database/information_about_companies.db")
    # # Создание курсора
    # cur = con.cursor()
    # result = cur.execute("""SELECT id FROM users WHERE id = ?""", (message.from_user.id, )).fetchone()
    # if result is None:
    #     cur.execute("""INSERT INTO users(id, name)
    #     VALUES(?, ?)""", (message.from_user.id, message.from_user.username, ))
    # con.commit()
    # con.close()
    await message.answer(f"Привет, {message.from_user.username}! Я - Телеграм-бот, который поможет тебе узнать больше про сборы и переработки отходов",
                         reply_markup=start_keyboard)


# Перемещение в гланое меню
@dp.message(F.text == "В главное меню⤵️")
async def start(message: types.Message):
    await message.answer("Вы в главном меню✅",
        reply_markup=start_keyboard)
