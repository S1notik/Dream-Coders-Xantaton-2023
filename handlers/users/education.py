from aiogram import types, F
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile
from keyboards.inline import *
from loader import dp
from keyboards.defoult.reply_buttons import education_keyboard
from keyboards.inline import question1_keyboard, question2_keyboard
import time
import sqlite3


con = sqlite3.connect("data/database/information_about_companies.db")
cur = con.cursor()
id = count = 0
main_flag = False


@dp.message(F.text == "Обучающие материалы📚")
async def education(message: types.Message):
    await message.answer("<b>Вы окунулись в мир образовательных материалов</b>📚",
                         reply_markup=education_keyboard, parse_mode=ParseMode.HTML)


# Useful links and video lessons
@dp.message(F.text == "Соц-Сети разработчиков🔗")
async def education(message: types.Message):
    await message.answer("Вот они):",
                         reply_markup=useful_links_inline_keyboard)
