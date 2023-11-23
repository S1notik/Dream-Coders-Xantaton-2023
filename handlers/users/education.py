from aiogram import types, F
from aiogram.filters import CommandStart
from keyboards.inline import useful_links_inline_keyboard, ecolesson_inline_keyboard
from loader import dp
from keyboards.defoult.reply_buttons import education_keyboard



@dp.message(F.text == "Обучающие материалы📚")
async def education(message: types.Message):
    await message.answer("Вы в обучающих материалах",
                         reply_markup=education_keyboard)


# Useful links and video lessons
@dp.message(F.text == "Полезные ссылки🔗")
async def education(message: types.Message):
    await message.answer("Наши соцсети и видеоуроки:",
                         reply_markup=useful_links_inline_keyboard)


# Ссылка на экоурок и его описание
@dp.message(F.text == "Экоурок🏫")
async def education(message: types.Message):
    await message.answer("Экоцентр «Югра Собирает» не только пункт приема вторсырья - это еще и образовательная площадка, на которой проходят лекции.\n\n"
                         "На Экоуроке будет наглядно показано какие виды отходов перерабатываются или нет, какая альтернатива есть одноразовым пластиковым вещам и что изготавливается из вторичного сырья."
                         " Посетители экоуроков узнают о раздельном сборе отходов и дальнейшем пути вторичного сырья из первых рук.",
                         reply_markup=ecolesson_inline_keyboard)
