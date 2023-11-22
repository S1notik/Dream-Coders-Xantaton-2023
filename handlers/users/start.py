from aiogram import types
from aiogram.filters import CommandStart
from loader import dp
from keyboards.defoult.reply_buttons import start_keyboard


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет! Я - Телеграм-бот, который поможет тебе узнать больше про сборы и переработки отходов в Югре.",
                         reply_markup=start_keyboard)