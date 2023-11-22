from aiogram import types, F
from loader import dp, bot
from aiogram.types import InputFile, ContentType, FSInputFile


@dp.message(F.text)
async def infografika(message: types.Message):
    if message.text == "Батарейки":
        await message.answer_photo(FSInputFile('Плакат_Батарейки.jpg'))
