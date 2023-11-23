from aiogram import types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from loader import dp
from aiogram import F


@dp.message(F.text == "Основные правила приёма📃")
async def basic_rules(message: types.Message):
    await message.answer("<b>Правила приёма📃:</b>\n"
                         "1. Сдаваемое сырье должно быть чистым.\n"
                         "2. Бутылки, банки, пакеты, пленки - без остатков пищи.\n"
                         "3. Металлические и пластиковые крышки необходимо снять с бутылок и банок.\n"
                         "4. Картон и бумага - чистые, не мокрые, без остатков пищи, без загрязнений, снять скрепки, скобы, убрать скотч и файлы.\n"
                         , parse_mode=ParseMode.HTML,
    )