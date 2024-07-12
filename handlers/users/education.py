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


# Ссылка на экоурок и его описание
@dp.message(F.text == "Экоурок🏫")
async def education(message: types.Message):
    await message.answer_photo(FSInputFile("data/image/logo_to_aco_lessons.jpg"))
    await message.answer("Экоцентр «Югра Собирает» не только пункт приема вторсырья - это еще и образовательная площадка, на которой проходят лекции.\n\n")

    time.sleep(1)

    await message.answer(
            "На Экоуроке будет наглядно показано <b>какие виды отходов перерабатываются</b> или нет, какая альтернатива есть одноразовым пластиковым вещам и что изготавливается из вторичного сырья."
            " Посетители экоуроков узнают о <ins>раздельном сборе отходов и дальнейшем пути вторичного сырья</ins> из первых рук.",
        reply_markup=ecolesson_inline_keyboard, parse_mode=ParseMode.HTML)


# Тест на 10 вопросов ---------------------------------------------------------------------------------------------

@dp.message(F.text == "Тест🏆")
async def start_test_question1(message: types.Message):
    await message.answer("❔О чем говорит этот значок ♻️? Его часто размещают на упаковке продуктов.",
                         reply_markup=question1_keyboard)
    global count, id, cur, main_flag
    main_flag = False
    cur = con.cursor()
    id = message.from_user.id
    count = 0


# Обработка ответов на первый вопрос ------------------------------------

@dp.callback_query(F.data == "answer1_question1_quiz")
async def question1(callback: types.CallbackQuery):
    global id, count, cur, con, count
    result = cur.execute("""SELECT q1 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        count += 1
        await callback.message.answer("✅Верно!\n\n")
        cur.execute(f"""UPDATE users SET q1={True} WHERE id = ?""", (id,))
        con.commit()
        con.close()
        await score_for_questions(id)
        con = sqlite3.connect("data/database/information_about_companies.db")
        cur = con.cursor()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Это правильный ответ")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Можно ли класть одноразовый стаканчик из-под кофе в контейнер для бумаги?",
                                  reply_markup=question2_keyboard)


@dp.callback_query(F.data == "answer2_question1_quiz")
async def question1(callback: types.CallbackQuery):
    global cur, con
    result = cur.execute("""SELECT q1 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                  "Правильный ответ: Материал упаковки может быть переработан или упаковка частично/полностью сделана из вторсырья")
        cur.execute(f"""UPDATE users SET q1={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: Материал упаковки может быть переработан или упаковка частично/полностью сделана из вторсырья")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                "Можно ли класть одноразовый стаканчик из-под кофе в контейнер для бумаги?",
                         reply_markup=question2_keyboard)


@dp.callback_query(F.data == "answer3_question1_quiz")
async def question1(callback: types.CallbackQuery):
    global cur, con
    result = cur.execute("""SELECT q1 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Материал упаковки может быть переработан или упаковка частично/полностью сделана из вторсырья")
        cur.execute(f"""UPDATE users SET q1={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: Материал упаковки может быть переработан или упаковка частично/полностью сделана из вторсырья")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                 "Можно ли класть одноразовый стаканчик из-под кофе в контейнер для бумаги?",
                         reply_markup=question2_keyboard)


# Обработка ответов на второй вопрос ------------------------------------

@dp.callback_query(F.data == "answer1_question2_quiz")
async def question2(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q2 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Нет, нельзя")
        cur.execute(f"""UPDATE users SET q2={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: Нет, нельзя")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Если кто-то из жильцов не платит за мусор, то...",
                                  reply_markup=question3_keyboard)


@dp.callback_query(F.data == "answer2_question2_quiz")
async def question2(callback: types.CallbackQuery):
    global id, count, cur, con, count
    result = cur.execute("""SELECT q2 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        count += 1
        await callback.message.answer("✅Верно!\n\n")
        cur.execute(f"""UPDATE users SET q2={True} WHERE id = ?""", (id,))
        con.commit()
        con.close()
        await score_for_questions(id)
        con = sqlite3.connect("data/database/information_about_companies.db")
        cur = con.cursor()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Это правильный ответ")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Если кто-то из жильцов не платит за мусор, то...",
                                  reply_markup=question3_keyboard)


@dp.callback_query(F.data == "answer3_question2_quiz")
async def question2(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q2 FROM users WHERE id = ?""", (id,)).fetchone()
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Нет, нельзя")
        cur.execute(f"""UPDATE users SET q2={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: Нет, нельзя")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Если кто-то из жильцов не платит за мусор, то...",
                                  reply_markup=question3_keyboard)


# Обработка ответов на третий вопрос ------------------------------------

@dp.callback_query(F.data == "answer1_question3_quiz")
async def question3(callback: types.CallbackQuery):
    global id, count, cur, con, count
    result = cur.execute("""SELECT q3 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        count += 1
        await callback.message.answer("✅Верно!\n\n")
        cur.execute(f"""UPDATE users SET q3={True} WHERE id = ?""", (id,))
        con.commit()
        con.close()
        await score_for_questions(id)
        con = sqlite3.connect("data/database/information_about_companies.db")
        cur = con.cursor()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Это правильный ответ")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Какую посуду ты берешь для отдыха на природе?",
                                  reply_markup=question4_keyboard)


@dp.callback_query(F.data == "answer2_question3_quiz")
async def question3(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q3 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Долг останется только за тем, кто допустил просрочку платежа")
        cur.execute(f"""UPDATE users SET q3={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: Долг останется только за тем, кто допустил просрочку платежа")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Какую посуду ты берешь для отдыха на природе?",
                                  reply_markup=question4_keyboard)


@dp.callback_query(F.data == "answer3_question3_quiz")
async def question3(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q3 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Долг останется только за тем, кто допустил просрочку платежа")
        cur.execute(f"""UPDATE users SET q3={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: Долг останется только за тем, кто допустил просрочку платежа")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Какую посуду ты берешь для отдыха на природе?",
                                  reply_markup=question4_keyboard)


# Обработка ответов на четвертый вопрос ------------------------------------

@dp.callback_query(F.data == "answer1_question4_quiz")
async def question4(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q4 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Обычно я во время прогулок на природе не ем")
        cur.execute(f"""UPDATE users SET q4={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: Обычно я во время прогулок на природе не ем")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Ты снимаешь квартиру. Кто должен платить за вывоз мусора?",
                                  reply_markup=question5_keyboard)


@dp.callback_query(F.data == "answer2_question4_quiz")
async def question4(callback: types.CallbackQuery):
    global id, count, cur, con, count
    result = cur.execute("""SELECT q4 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        count += 1
        await callback.message.answer("✅Верно!\n\n")
        cur.execute(f"""UPDATE users SET q4={True} WHERE id = ?""", (id,))
        con.commit()
        con.close()
        await score_for_questions(id)
        con = sqlite3.connect("data/database/information_about_companies.db")
        cur = con.cursor()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Это правильный ответ")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Ты снимаешь квартиру. Кто должен платить за вывоз мусора?",
                                  reply_markup=question5_keyboard)


@dp.callback_query(F.data == "answer3_question4_quiz")
async def question4(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q4 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Обычно я во время прогулок на природе не ем")
        cur.execute(f"""UPDATE users SET q4={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: Обычно я во время прогулок на природе не ем")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Ты снимаешь квартиру. Кто должен платить за вывоз мусора?",
                                  reply_markup=question5_keyboard)


# Обработка ответов на пятый вопрос ------------------------------------

@dp.callback_query(F.data == "answer1_question5_quiz")
async def question5(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q5 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: В зависимости от договоренностей хозяина и арендатора")
        cur.execute(f"""UPDATE users SET q5={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: В зависимости от договоренностей хозяина и арендатора")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Сколько воды ты выпиваешь за день?",
                                  reply_markup=question6_keyboard)


@dp.callback_query(F.data == "answer2_question5_quiz")
async def question5(callback: types.CallbackQuery):
    global id, count, cur, con, count
    result = cur.execute("""SELECT q5 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        count += 1
        await callback.message.answer("✅Верно!\n\n")
        cur.execute(f"""UPDATE users SET q5={True} WHERE id = ?""", (id,))
        con.commit()
        con.close()
        await score_for_questions(id)
        con = sqlite3.connect("data/database/information_about_companies.db")
        cur = con.cursor()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Это правильный ответ")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Сколько воды ты выпиваешь за день?",
                                  reply_markup=question6_keyboard)


@dp.callback_query(F.data == "answer3_question5_quiz")
async def question5(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q5 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: В зависимости от договоренностей хозяина и арендатора")
        cur.execute(f"""UPDATE users SET q5={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: В зависимости от договоренностей хозяина и арендатора")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Сколько воды ты выпиваешь за день?",
                                  reply_markup=question6_keyboard)


# Обработка ответов на шестой вопрос ------------------------------------

@dp.callback_query(F.data == "answer1_question6_quiz")
async def question6(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q6 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Я каждое утро беру с собой термос с питьевой водой")
        cur.execute(f"""UPDATE users SET q6={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: Я каждое утро беру с собой термос с питьевой водой")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Куда следует приносить документы для перерасчета?",
                                  reply_markup=question7_keyboard)


@dp.callback_query(F.data == "answer2_question6_quiz")
async def question6(callback: types.CallbackQuery):
    global id, count, cur, con, count
    result = cur.execute("""SELECT q6 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        count += 1
        await callback.message.answer("✅Верно!\n\n")
        cur.execute(f"""UPDATE users SET q6={True} WHERE id = ?""", (id,))
        con.commit()
        con.close()
        await score_for_questions(id)
        con = sqlite3.connect("data/database/information_about_companies.db")
        cur = con.cursor()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Это правильный ответ")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Куда следует приносить документы для перерасчета?",
                                  reply_markup=question7_keyboard)


@dp.callback_query(F.data == "answer3_question6_quiz")
async def question6(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q6 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Я каждое утро беру с собой термос с питьевой водой")
        cur.execute(f"""UPDATE users SET q6={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: Я каждое утро беру с собой термос с питьевой водой")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Куда следует приносить документы для перерасчета?",
                                  reply_markup=question7_keyboard)


# Обработка ответов на седьмой вопрос ------------------------------------

@dp.callback_query(F.data == "answer1_question7_quiz")
async def question7(callback: types.CallbackQuery):
    global id, count, cur, con, count
    result = cur.execute("""SELECT q7 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        count += 1
        await callback.message.answer("✅Верно!\n\n")
        cur.execute(f"""UPDATE users SET q7={True} WHERE id = ?""", (id,))
        con.commit()
        con.close()
        await score_for_questions(id)
        con = sqlite3.connect("data/database/information_about_companies.db")
        cur = con.cursor()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Это правильный ответ")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Какие из этих предметов опасно выбрасывать в обычное мусорное ведро?",
                                  reply_markup=question8_keyboard)


@dp.callback_query(F.data == "answer2_question7_quiz")
async def question7(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q7 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: В офис агентов по расчетно-кассовому обслуживанию")
        cur.execute(f"""UPDATE users SET q7={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: В офис агентов по расчетно-кассовому обслуживанию")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Какие из этих предметов опасно выбрасывать в обычное мусорное ведро?",
                                  reply_markup=question8_keyboard)


@dp.callback_query(F.data == "answer3_question7_quiz")
async def question7(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q7 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: В офис агентов по расчетно-кассовому обслуживанию")
        cur.execute(f"""UPDATE users SET q7={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: В офис агентов по расчетно-кассовому обслуживанию")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Какие из этих предметов опасно выбрасывать в обычное мусорное ведро?",
                                  reply_markup=question8_keyboard)


# Обработка ответов на восьмой вопрос ------------------------------------

@dp.callback_query(F.data == "answer1_question8_quiz")
async def question8(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q8 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Батарейки")
        cur.execute(f"""UPDATE users SET q8={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: Батарейки")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Что из оставленного туристами в лесу быстрее разложится?",
                                  reply_markup=question9_keyboard)


@dp.callback_query(F.data == "answer2_question8_quiz")
async def question8(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q8 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Батарейки")
        cur.execute(f"""UPDATE users SET q8={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: Батарейки")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Что из оставленного туристами в лесу быстрее разложится?",
                                  reply_markup=question9_keyboard)


@dp.callback_query(F.data == "answer3_question8_quiz")
async def question8(callback: types.CallbackQuery):
    global id, count, cur, con, count
    result = cur.execute("""SELECT q8 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        count += 1
        await callback.message.answer("✅Верно!\n\n")
        cur.execute(f"""UPDATE users SET q8={True} WHERE id = ?""", (id,))
        con.commit()
        con.close()
        await score_for_questions(id)
        con = sqlite3.connect("data/database/information_about_companies.db")
        cur = con.cursor()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Это правильный ответ")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Что из оставленного туристами в лесу быстрее разложится?",
                                  reply_markup=question9_keyboard)


# Обработка ответов на девятый вопрос ------------------------------------

@dp.callback_query(F.data == "answer1_question9_quiz")
async def question9(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q9 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Железная консервная банка")
        cur.execute(f"""UPDATE users SET q9={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\nПравильный ответ: Железная консервная банка")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Какая упаковка яиц менее вредна для экологии?",
                                  reply_markup=question10_keyboard)


@dp.callback_query(F.data == "answer2_question9_quiz")
async def question9(callback: types.CallbackQuery):
    global cur
    result = cur.execute("""SELECT q9 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Железная консервная банка")
        cur.execute(f"""UPDATE users SET q9={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\nПравильный ответ: Железная консервная банка")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Какая упаковка яиц менее вредна для экологии?",
                                  reply_markup=question10_keyboard)


@dp.callback_query(F.data == "answer3_question9_quiz")
async def question9(callback: types.CallbackQuery):
    global id, count, cur, con, count
    result = cur.execute("""SELECT q9 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        count += 1
        await callback.message.answer("✅Верно!\n\n")
        cur.execute(f"""UPDATE users SET q9={True} WHERE id = ?""", (id,))
        con.commit()
        con.close()
        await score_for_questions(id)
        con = sqlite3.connect("data/database/information_about_companies.db")
        cur = con.cursor()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Это правильный ответ")
    time.sleep(1.5)
    await callback.message.answer("❔Следующий вопрос:\n"
                                  "Какая упаковка яиц менее вредна для экологии?",
                                  reply_markup=question10_keyboard)


# Обработка ответов на десятый вопрос ------------------------------------
@dp.callback_query(F.data == "answer1_question10_quiz")
async def question10(callback: types.CallbackQuery):
    global id, count, cur, con, count, main_flag
    result = cur.execute("""SELECT q10 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        count += 1
        await callback.message.answer("✅Верно!\n\n")
        cur.execute(f"""UPDATE users SET q10={True} WHERE id = ?""", (id,))
        con.commit()
        con.close()
        await score_for_questions(id)
        con = sqlite3.connect("data/database/information_about_companies.db")
        cur = con.cursor()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Это правильный ответ")
    time.sleep(1.5)
    await callback.message.answer(f"Поздравляю!🎉 Вы полностью прошли тест🎊. Ваши баллы {count}/10\n\n"
                                  "Надеюсь, вы узнали для себя что-то новое😄")
    if not main_flag:
        await callback.message.answer(f"Вам зачислено {count * 10} опыта")
        main_flag = False


@dp.callback_query(F.data == "answer2_question10_quiz")
async def question10(callback: types.CallbackQuery):
    global cur, main_flag
    result = cur.execute("""SELECT q10 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Упаковка из прессованной макулатуры")
        cur.execute(f"""UPDATE users SET q10={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: Упаковка из прессованной макулатуры")
    time.sleep(1.5)
    await callback.message.answer(f"Поздравляю!🎉 Вы полностью прошли тест🎊. Ваши баллы {count}/10\n\n"
                                  "Надеюсь, вы узнали для себя что-то новое😄")
    if not main_flag:
        await callback.message.answer(f"Вам зачислено {count * 10} опыта")
        main_flag = True


@dp.callback_query(F.data == "answer3_question10_quiz")
async def question10(callback: types.CallbackQuery):
    global cur, main_flag
    result = cur.execute("""SELECT q10 FROM users WHERE id = ?""", (id,)).fetchone()[0]
    if not result:
        await callback.message.answer("❌Неверно!\n\n"
                                      "Правильный ответ: Упаковка из прессованной макулатуры")
        cur.execute(f"""UPDATE users SET q10={True} WHERE id = ?""", (id,)).fetchone()
        con.commit()
    else:
        await callback.message.answer("Вы уже ответили на данный вопрос!\n"
                                      "Правильный ответ: Упаковка из прессованной макулатуры")
    time.sleep(1.5)
    await callback.message.answer(f"Поздравляю!🎉 Вы полностью прошли тест🎊. Ваши баллы {count}/10\n\n" 
                                  "Надеюсь, вы узнали для себя что-то новое😄")
    if not main_flag:
        await callback.message.answer(f"Вам зачислено {count * 10} опыта")
        main_flag = True


async def score_for_questions(id):
    con = sqlite3.connect("data/database/information_about_companies.db")
    cur = con.cursor()
    score = cur.execute(f'''SELECT score FROM users WHERE id = {id}''').fetchone()[0]
    cur.execute(f"""UPDATE users SET score={score + 10 if score else 10} WHERE id={id}""")
    con.commit()
    con.close()
