from aiogram import types
from aiogram import F
from aiogram.enums import ParseMode

from keyboards.inline import types_materials_inline_keyboard
from loader import dp


@dp.message(F.text == "Виды сырья🗑️")
async def types_materials(message: types.Message):
    await message.answer("♻️<b>Ниже вы можете ознакомиться с <ins>правилами приёма</ins> различных отходов:  </b>", parse_mode=ParseMode.HTML, reply_markup=types_materials_inline_keyboard)


@dp.callback_query(F.data == "glass_bottles_and_jars_typematerial")
async def glass_bottles_and_jars(callback: types.CallbackQuery):
    await callback.message.answer("<b>Коричневые, зеленые и бесцветные стеклянные бутылки и банки:</b>\n\n"
                         "-Баллы за 1 килограмм: 1\n\n"
                         "-<ins>Правила приема:</ins>\n"
                         "\t✅ Чистые, без крышек и ободков, бумажные этикетки можно не убирать\n"
                         "\t✅ Необходимо сдавать по отдельности коричневое, зеленое и бесцветное стекло",
                                  parse_mode=ParseMode.HTML)


@dp.callback_query(F.data == "waste_paper_typematerial")
async def waste_paper(callback: types.CallbackQuery):
    await callback.message.answer("<b>Макулатура:</b>\n\n"
                         "-Баллы за 1 килограмм: 2\n\n"
                         "-<ins>Правила приема:</ins>\n"
                         "\t✅ Книги, газеты, журналы, бумага, гофрокартон\n"
                         "\t✅ Чистое, сложенное в коробки или перевязанное, без жирных пятен и остатков еды, без файлов и скрепок\n\n"
                         "-<ins>Не принимется:</ins>\n"
                         "\t❌ Одноразовая посуда, обои, чеки, пачки сигарет, мешки от строительных смесей, упаковка из пульперкартона, гофроупаковка от яиц",
                                  parse_mode=ParseMode.HTML)


@dp.callback_query(F.data == "HDPE_plastic_boxes_typematerial")
async def HDPE_plastic_boxes(callback: types.CallbackQuery):
    await callback.message.answer("<b>Пластиковые ящики ПНД:</b>\n\n"
                         "-Баллы за 1 килограмм: 5\n\n"
                         "-<ins>Правила приема:</ins>\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Всех размеров, цветов и толщины",
                                  parse_mode=ParseMode.HTML)


@dp.callback_query(F.data == "batteries_typematerial")
async def batteries(callback: types.CallbackQuery):
    await callback.message.answer("<b>Батарейки:</b>\n\n"
                        "-Баллы за 1 килограмм: 20\n\n"
                        "-<ins>Правила приема:</ins>\n"
                        "\t✅ Любых типов и брендов\n",
                                  parse_mode=ParseMode.HTML)


@dp.callback_query(F.data == "HDPE_LDPE_canisters_typematerial")
async def HDPE_LDPE_canisters(callback: types.CallbackQuery):
    await callback.message.answer("<b>Канистры ПНД, ПВД:</b>\n\n"
                         "-Баллы за 1 килограмм: 5\n\n"
                         "-<ins>Правила приема:</ins>\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Всех размеров и цветов, в том числе от моторного масла\n\n"
                         "-<ins>Не принимется:</ins>\n"
                         "\t❌ Канистры из под химических веществ, кислот, целочей и пр.",
                                  parse_mode=ParseMode.HTML)


@dp.callback_query(F.data == "LDPE_Stretch_film_typematerial")
async def LDPE_Stretch_film(callback: types.CallbackQuery):
    await callback.message.answer("<b>Стретч-пленка ПВД:</b>\n\n"
                         "-Баллы за 1 килограмм: 7\n\n"
                         "-<ins>Правила приема:</ins>\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Необходимо удалить скотч, наклейки\n"
                         "\t✅ Принимается отдельно от других видов пленки",
                                  parse_mode=ParseMode.HTML)


@dp.callback_query(F.data == "LDPE_film_typematerial")
async def LDPE_film(callback: types.CallbackQuery):
    await callback.message.answer("<b>Пленка ПВД:</b>\n\n"
                         "-Баллы за 1 килограмм: 7\n\n"
                         "-<ins>Правила приема:</ins>\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Необходимо удалить скотч, наклейки, срезать “застежки\n"
                         "\t✅ Плёнки можно сдавать вместе, не разделяя по видам",
                                  parse_mode=ParseMode.HTML)


@dp.callback_query(F.data == "HDPE_LDPE_PP_covers_typematerial")
async def HDPE_LDPE_PP_covers(callback: types.CallbackQuery):
    await callback.message.answer("<b>Крышки ПНД, ПВД, ПП:</b>\n\n"
                         "-Баллы за 1 килограмм: 15\n\n"
                         "-<ins>Правила приема:</ins>\n"
                         "\t✅ Чистые, cнять этикетки, вкладыши\n"
                         "\t✅ Только с маркировкой 2, 4, 5\n\n"
                         "-<ins>Не принимется:</ins>\n"
                         "\t❌ Крышки металлические, стеклянные, пробковые, из пластика маркировки 6 (от одноразовых стаканчиков)",
                                  parse_mode=ParseMode.HTML)


@dp.callback_query(F.data == "white_PET_bottles_from_drinks_typematerial")
async def white_PET_bottles_from_drinks(callback: types.CallbackQuery):
    await callback.message.answer("<b>Белые ПЭТ-бутылки от напитков:</b>\n\n"
                         "-Баллы за 1 килограмм: 5\n\n"
                         "-<ins>Правила приема:</ins>\n"
                         "\t✅ Чистые, cнять этикетки, вкладыши\n"
                         "\t✅ Только с маркировкой 2, 4, 5",
                                  parse_mode=ParseMode.HTML)


@dp.callback_query(F.data == "packing_packages_and_packagesTshirts_of_HDPE_LDPE_typematerial")
async def packing_packages_and_packagesTshirts_of_HDPE_LDPE(callback: types.CallbackQuery):
    await callback.message.answer("<b>Пакеты фасовочные и пакеты-майки ПНД, ПВД:</b>\n\n"
                         "-Баллы за 1 килограмм: 7\n\n"
                         "-<ins>Правила приема:</ins>\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Без скотча и наклеек",
                                  parse_mode=ParseMode.HTML)

@dp.callback_query(F.data == "PET_bottles_from_beverages_and_vegetable_oil_typematerial")
async def PET_bottles_from_beverages_and_vegetable_oil(callback: types.CallbackQuery):
    await callback.message.answer("<b>ПЭТ-бутылки от напитков и растительного масла:</b>\n\n"
                         "-Баллы за 1 килограмм: 5\n\n"
                         "-<ins>Правила приема:</ins>\n"
                         "\t✅ Чистые, спрессованные, с маркировкой\n"
                         "\t✅ Крышки необходимо откручивать и сдавать отдельно\n\n"
                         "-<ins>Не принимется:</ins>\n"
                         "\t❌ Бутылки ярко-кислотных цветов\n"
                         "\t❌ Бутылки кулерные 19-литровые\n"
                         "\t❌ Бутылки от бытовой химии и белые ПЭТ-бутылки принимаются отдельно\n",
                                  parse_mode=ParseMode.HTML)


@dp.callback_query(F.data == "aluminum_cans_typematerial")
async def aluminum_cans(callback: types.CallbackQuery):
    await callback.message.answer("<b>Алюминиевые банки:</b>\n\n"
                         "-Баллы за 1 килограмм: 10\n\n"
                         "-<ins>Правила приема:</ins>\n"
                         "\t✅ Чистые, спресованные",
                                  parse_mode=ParseMode.HTML)



