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
@dp.message(F.text == "Полезные ссылки🔗")
async def education(message: types.Message):
    await message.answer("Наши соцсети и видеоуроки:",
                         reply_markup=useful_links_inline_keyboard)



# Тест на 10 вопросов ---------------------------------------------------------------------------------------------
#
# @dp.message(F.text == "Тест🏆")
# async def start_test_question1(message: types.Message):
#     await message.answer("❔О чем говорит этот значок ♻️? Его часто размещают на упаковке продуктов.",
#                          reply_markup=question1_keyboard)
#     global count, id, cur, main_flag
#     main_flag = False
#     cur = con.cursor()
#     id = message.from_user.id
#     count = 0
#

# Подсчет очков для теста
# async def score_for_questions(id):
#     con = sqlite3.connect("data/database/information_about_companies.db")
#     cur = con.cursor()
#     score = cur.execute(f'''SELECT score FROM users WHERE id = {id}''').fetchone()[0]
#     cur.execute(f"""UPDATE users SET score={score + 10 if score else 10} WHERE id={id}""")
#     con.commit()
#     con.close()
