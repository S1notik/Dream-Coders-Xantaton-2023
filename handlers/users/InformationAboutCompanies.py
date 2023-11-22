from aiogram.enums import ParseMode

from loader import dp, bot
from aiogram import F, types


@dp.message(F.text == "Пункты сбора♻️")
async def iac(message: types.Message):  # Information about companies
    await message.answer("Про какие пункты сбора вы хотите узнать?")


@dp.message(F.text == "ХАНТЫ-МАНСИЙСК🌁")
async def xmao(message: types.Message):
    await bot.send_location(message.from_user.id, 61.003895, 69.051789)
    await message.answer("<ins>Адресс:</ins> г. Ханты-Мансийск ул. Чехова, д. 74\n"
                         "<ins>Ежедневно:</ins> 10:00 - 20:00\n"
                         "<ins>Обед</ins>: 14:00 - 15:00\n"
                         "<ins>Тех. перерывы</ins>: 11:45 - 12:00 / 16:45 - 17:00\n"
                         "<ins>", parse_mode=ParseMode.HTML
                         )



