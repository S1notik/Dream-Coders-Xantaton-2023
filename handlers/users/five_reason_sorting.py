from aiogram import F, types
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile
import time
from loader import dp


@dp.callback_query(F.data == "reasons_to_sort")
async def reasons_to_sort(callback: types.CallbackQuery):
    await callback.message.answer_photo(FSInputFile("data/image/img_sort.png"))
    await callback.message.answer("1. <b>Экономия природных ресурсов</b>", parse_mode=ParseMode.HTML)
    time.sleep(2)
    await callback.message.answer("2. <b>Уменьшение объёмов отходов, размещаемых на полигонах</b>",
                                  parse_mode=ParseMode.HTML)
    time.sleep(2)
    await callback.message.answer("3. <b>Повторное использование ресурсов и снижение затрат "
                                  "на производство новых изделий</b>",
                                  parse_mode=ParseMode.HTML)
    time.sleep(2)
    await callback.message.answer("4. <b>Бонус, за сдачу правильно подготовленного вторичного "
                                  "сырья</b>", parse_mode=ParseMode.HTML)
    time.sleep(2)
    await callback.message.answer("5. <b>Повышение уровня осознанности</b>", parse_mode=ParseMode.HTML)

