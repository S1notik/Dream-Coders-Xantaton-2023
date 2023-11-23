from aiogram import types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile

from keyboards.inline import useful_links_inline_keyboard, ecolesson_inline_keyboard
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


# Тест на 10 вопросов

@dp.message(F.text == "Тест🏆")
async def start_test_question1(message: types.Message):
    await message.answer("О чем говорит этот значок ♻️? Его часто размещают на упаковке продуктов.",
                         reply_markup=question1_keyboard)

@dp.callback_query(F.data == "answer1_question1_quiz")
async def question2(callback: types.CallbackQuery):
    await callback.message.answer("Верно!\n\n"
                         "Следующий вопрос:\n"
                         "Можно ли класть одноразовый стаканчик из-под кофе в контейнер для бумаги?",
                         reply_markup=question2_keyboard)

@dp.callback_query(F.data == "answer2_question1_quiz")
async def question2(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n"
                         "Следующий вопрос:\n"
                         "Можно ли класть одноразовый стаканчик из-под кофе в контейнер для бумаги?",
                         reply_markup=question2_keyboard)

@dp.callback_query(F.data == "answer3_question1_quiz")
async def question2(callback: types.CallbackQuery):
    await callback.message.answer("Неверно!\n\n"
                         "Следующий вопрос:\n"
                         "Можно ли класть одноразовый стаканчик из-под кофе в контейнер для бумаги?",
                         reply_markup=question2_keyboard)

