from aiogram import types, F
from aiogram.filters import CommandStart
from loader import dp
from keyboards.defoult.reply_buttons import education_keyboard



@dp.message(F.text == "Обучающие материалы📚")
async def education(message: types.Message):
    await message.answer("Вы в обучающих материалах",
                         reply_markup=education_keyboard)