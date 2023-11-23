from aiogram import types, F
from aiogram.filters import CommandStart
from keyboards.inline import useful_links_inline_keyboard
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
