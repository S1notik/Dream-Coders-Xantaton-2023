from aiogram import types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile

from keyboards.inline import *
from loader import dp
from keyboards.defoult.reply_buttons import education_keyboard
from keyboards.inline import question1_keyboard, question2_keyboard
import time



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
    await message.answer("О чем говорит этот значок ♻️? Его часто размещают на упаковке продуктов.",
                         reply_markup=question1_keyboard)


# Обработка ответов на первый вопрос ------------------------------------
question1 = "Следующий вопрос:\n" \
           "Можно ли класть одноразовый стаканчик из-под кофе в контейнер для бумаги?"

@dp.callback_query(F.data == "answer1_question1_quiz")
async def question1(callback: types.CallbackQuery):
    await callback.message.answer("Верно!\n\n" + question1,
                         reply_markup=question2_keyboard)

@dp.callback_query(F.data == "answer2_question1_quiz")
async def question1(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question1,
                         reply_markup=question2_keyboard)

@dp.callback_query(F.data == "answer3_question1_quiz")
async def question1(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question1,
                         reply_markup=question2_keyboard)


# Обработка ответов на второй вопрос ------------------------------------
question2 = "Следующий вопрос:\n" \
           "Если кто-то из жильцов не платит за мусор, то..."
@dp.callback_query(F.data == "answer1_question2_quiz")
async def question2(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question2,
                         reply_markup=question3_keyboard)

@dp.callback_query(F.data == "answer2_question2_quiz")
async def question2(callback: types.CallbackQuery):
    await callback.message.answer("Верно!\n\n" + question2,
                         reply_markup=question3_keyboard)

@dp.callback_query(F.data == "answer3_question2_quiz")
async def question2(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question2,
                         reply_markup=question3_keyboard)


# Обработка ответов на третий вопрос ------------------------------------
question3 = "Следующий вопрос:\n" \
            "Какую посуду ты берешь для отдыха на природе?"

@dp.callback_query(F.data == "answer1_question3_quiz")
async def question3(callback: types.CallbackQuery):
    await callback.message.answer("Верно!\n\n" + question3,
                         reply_markup=question4_keyboard)

@dp.callback_query(F.data == "answer2_question3_quiz")
async def question3(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question3,
                         reply_markup=question4_keyboard)

@dp.callback_query(F.data == "answer3_question3_quiz")
async def question3(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question3,
                         reply_markup=question4_keyboard)


# Обработка ответов на четвертый вопрос ------------------------------------
question4 = "Следующий вопрос:\n" \
            "Ты снимаешь квартиру. Кто должен платить за вывоз мусора?"

@dp.callback_query(F.data == "answer1_question4_quiz")
async def question4(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question4,
                         reply_markup=question5_keyboard)

@dp.callback_query(F.data == "answer2_question4_quiz")
async def question4(callback: types.CallbackQuery):
    await callback.message.answer("Верно!\n\n" + question4,
                         reply_markup=question5_keyboard)

@dp.callback_query(F.data == "answer3_question4_quiz")
async def question4(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question4,
                         reply_markup=question5_keyboard)


# Обработка ответов на пятый вопрос ------------------------------------
question5 = "Следующий вопрос:\n" \
            "Сколько воды ты выпиваешь за день?"

@dp.callback_query(F.data == "answer1_question5_quiz")
async def question5(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question5,
                         reply_markup=question6_keyboard)

@dp.callback_query(F.data == "answer2_question5_quiz")
async def question5(callback: types.CallbackQuery):
    await callback.message.answer("Верно!\n\n" + question5,
                         reply_markup=question6_keyboard)

@dp.callback_query(F.data == "answer3_question5_quiz")
async def question5(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question5,
                         reply_markup=question6_keyboard)


# Обработка ответов на шестой вопрос ------------------------------------
question6 = "Следующий вопрос:\n" \
            "Куда следует приносить документы для перерасчета?"

@dp.callback_query(F.data == "answer1_question6_quiz")
async def question6(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question6,
                         reply_markup=question7_keyboard)

@dp.callback_query(F.data == "answer2_question6_quiz")
async def question6(callback: types.CallbackQuery):
    await callback.message.answer("Верно!\n\n" + question6,
                         reply_markup=question7_keyboard)

@dp.callback_query(F.data == "answer3_question6_quiz")
async def question6(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question6,
                         reply_markup=question7_keyboard)


# Обработка ответов на седьмой вопрос ------------------------------------
question7 = "Следующий вопрос:\n" \
            "Какие из этих предметов опасно выбрасывать в обычное мусорное ведро?"

@dp.callback_query(F.data == "answer1_question7_quiz")
async def question7(callback: types.CallbackQuery):
    await callback.message.answer("Верно!\n\n" + question7,
                         reply_markup=question8_keyboard)

@dp.callback_query(F.data == "answer2_question7_quiz")
async def question7(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question7,
                         reply_markup=question8_keyboard)

@dp.callback_query(F.data == "answer3_question7_quiz")
async def question7(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question7,
                         reply_markup=question8_keyboard)


# Обработка ответов на восьмой вопрос ------------------------------------
question8 = "Следующий вопрос:\n" \
            "Что из оставленного туристами в лесу быстрее разложится?"

@dp.callback_query(F.data == "answer1_question8_quiz")
async def question8(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question8,
                         reply_markup=question9_keyboard)

@dp.callback_query(F.data == "answer2_question8_quiz")
async def question8(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question8,
                         reply_markup=question9_keyboard)

@dp.callback_query(F.data == "answer3_question8_quiz")
async def question8(callback: types.CallbackQuery):
    await callback.message.answer("Верно!\n\n" + question8,
                         reply_markup=question9_keyboard)


# Обработка ответов на девятый вопрос ------------------------------------
question9 = "Следующий вопрос:\n" \
            "Какая упаковка яиц менее вредна для экологии?"

@dp.callback_query(F.data == "answer1_question9_quiz")
async def question9(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question9,
                         reply_markup=question10_keyboard)

@dp.callback_query(F.data == "answer2_question9_quiz")
async def question9(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question9,
                         reply_markup=question10_keyboard)

@dp.callback_query(F.data == "answer3_question9_quiz")
async def question9(callback: types.CallbackQuery):
    await callback.message.answer("Верно!\n\n" + question9,
                         reply_markup=question10_keyboard)


# Обработка ответов на десятый вопрос ------------------------------------
question10 = "Поздравляю!🎉 Вы полностью прошли тест🎊\n\n" \
           "Надеюсь, вы узнали для себя что-то новое😄"

@dp.callback_query(F.data == "answer1_question10_quiz")
async def question10(callback: types.CallbackQuery):
    await callback.message.answer("Верно!\n\n" + question10)

@dp.callback_query(F.data == "answer2_question10_quiz")
async def question10(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question10)

@dp.callback_query(F.data == "answer3_question10_quiz")
async def question10(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n" + question10)
