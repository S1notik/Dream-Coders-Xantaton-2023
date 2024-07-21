from aiogram import types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from loader import dp
from aiogram import F


@dp.message(F.text == "Правила приёма📃")
async def basic_rules(message: types.Message):
    await message.answer("<b>Правила приёма📃:</b>\n\n"
                         "1. Сдаваемое сырье должно быть <ins>чистым</ins>.\n"
                         "2. Бутылки, банки, пакеты, пленки - <ins>без остатков пищи</ins>.\n"
                         "3. Металлические и пластиковые <ins>крышки необходимо снять</ins> с бутылок и банок.\n"
                         "4. Картон и бумага - <ins>чистые, не мокрые, без остатков пищи, без загрязнений, снять скрепки, скобы, убрать скотч и файлы</ins>.\n"
                         , parse_mode=ParseMode.HTML,
    )
