from aiogram.filters import CommandStart
from loader import dp
from keyboards.defoult.reply_buttons import start_keyboard
from aiogram import types, F


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет! Я - Телеграм-бот, который поможет тебе узнать больше про сборы и переработки отходов в Югре.",
                         reply_markup=start_keyboard)

# Перемещение в гланое меню
@dp.message(F.text == "В главное меню⤵️")
async def start(message: types.Message):
    await message.answer("Вы в главном меню✅",
        reply_markup=start_keyboard)
