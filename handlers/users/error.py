from aiogram import types
from loader import dp


@dp.message()
async def command_error(message: types.Message):
    await message.answer("Извините, я вас не понял")