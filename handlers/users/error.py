from aiogram import types

from keyboards.defoult import start_keyboard
from loader import dp


@dp.message()
async def command_error(message: types.Message):
    await message.answer("Извините, я вас не понял🤷‍♂️", reply_markup=start_keyboard)