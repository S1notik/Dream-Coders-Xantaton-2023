from aiogram import types, F
from aiogram.filters import CommandStart
from keyboards.inline import question1_keyboard, question2_keyboard
from loader import dp
from keyboards.defoult.reply_buttons import education_keyboard


@dp.message(F.text == "Тест🏆")
async def start_test_question1(message: types.Message):
    await message.answer("О чем говорит этот значок ♻️? Его часто размещают на упаковке продуктов.",
                         reply_markup=question1_keyboard)

@dp.callback_query(F.data == "answer1_question2_quiz")
async def question2(message: types.Message):
    await message.answer("Верно!\n\n"
                         "Следующий вопрос:\n"
                         "Можно ли класть одноразовый стаканчик из-под кофе в контейнер для бумаги?",
                         reply_markup=question2_keyboard)

@dp.callback_query(F.data == "answer2_question2_quiz")
async def question2(message: types.Message):
    await message.answer("Неверно!\n\n"
                         "Следующий вопрос:\n"
                         "Можно ли класть одноразовый стаканчик из-под кофе в контейнер для бумаги?",
                         reply_markup=question2_keyboard)

@dp.callback_query(F.data == "answer3_question2_quiz")
async def question2(message: types.Message):
    await message.answer("Неверно!\n\n"
                         "Следующий вопрос:\n"
                         "Можно ли класть одноразовый стаканчик из-под кофе в контейнер для бумаги?",
                         reply_markup=question2_keyboard)
