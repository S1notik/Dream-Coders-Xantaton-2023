import time

from aiogram import F, types
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile

from loader import dp
from keyboards.inline.inline_buttons import interesting_facts_inline_keyboard


@dp.message(F.text == "Интересные факты⭐️")
async def interesting_facts(message: types.Message):
    await message.answer("Выбирите интересующийся вами факт", reply_markup=interesting_facts_inline_keyboard)  # подключть инлайновые копки


@dp.callback_query(F.data == "where_the_waste_is_sent_for_recycling")  # КУДА НАПРАВЛЯЮТСЯ ОТХОДЫ НА ПЕРЕРАБОТКУ
async def where_is_pereraborka(callback: types.CallbackQuery):
    await callback.message.answer_photo(FSInputFile("data/image/map_of_city.png"))
    await callback.message.answer(
        "<b>Отходы принимаются и взвешиваются отдельно каждая фракция, далее отправляются на переработку.</b>"
        "<i>Некоторые фракции востребованы в Ханты-Мансийске. Есть предприятие по изготовлению тротуарной "
        "плитки из переработанного пластика.</i>", parse_mode=ParseMode.HTML)
    time.sleep(4.5)
    await callback.message.answer(
        "<i>ПЭТ-бутылка вывозится на завод в Екатеринбург, <ins>стекло</ins> будет вывозится в <ins>Тюменскую область</ins>,"
        " <ins>макулатура</ins> отправляется на заводы в <ins>Пермский край и Свердловскую область</ins>, <ins>батарейки</ins> "
        "вывозятся <ins>Национальной экологической компанией в Ярославль самостоятельно</ins>. Это рынок, и когда будет востребован"
        " другой вид вторсырья, мы расширим список.</i>",
        parse_mode=ParseMode.HTML
    )
    time.sleep(5)
    await callback.message.answer(
        "<b>На сегодня 15 фракций — это тоже много.</b> <i>Важно понимать, что это не отправляется на полигон, из экоцентра все"
        " вывозится на переработку.</i>",
        parse_mode=ParseMode.HTML
    )
    #

