from aiogram import types
from aiogram.filters import CommandStart
from aiogram import Bot, Dispatcher, F

from keyboards.inline import types_materials_inline_keyboard
from loader import dp


@dp.message(F.text == "Виды сырья🗑️")
async def types_materials(message: types.Message):
    await message.answer("В этом разжеле вы узнате о правилах приёма разлычных отходов", reply_markup=types_materials_inline_keyboard)


@dp.callback_query(F.data == "glass_bottles_and_jars_typematerial")
async def glass_bottles_and_jars(callback: types.CallbackQuery):
    await callback.message.answer("Коричневые, зеленые и бесцветные стеклянные бутылки и банки:\n\n"
                         "-Баллы за 1 килограмм: 1\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, без крышек и ободков, бумажные этикетки можно не убирать\n"
                         "\t✅ Необходимо сдавать по отдельности коричневое, зеленое и бесцветное стекло")


@dp.callback_query(F.data == "waste_paper_typematerial")
async def waste_paper(callback: types.CallbackQuery):
    await callback.message.answer("Макулатура:\n\n"
                         "-Баллы за 1 килограмм: 2\n\n"
                         "-Правила приема:\n"
                         "\t✅ Книги, газеты, журналы, бумага, гофрокартон\n"
                         "\t✅ Чистое, сложенное в коробки или перевязанное, без жирных пятен и остатков еды, без файлов и скрепок")


@dp.callback_query(F.data == "HDPE_plastic_boxes_typematerial")
async def HDPE_plastic_boxes(callback: types.CallbackQuery):
    await callback.message.answer("Пластиковые ящики ПНД:\n\n"
                         "-Баллы за 1 килограмм: 5\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Всех размеров, цветов и толщины")


@dp.callback_query(F.data == "batteries_typematerial")
async def batteries(callback: types.CallbackQuery):
    await callback.message.answer("Батарейки:\n\n"
                        "-Баллы за 1 килограмм: 20\n\n"
                        "-Правила приема:\n"
                        "\t✅ Любых типов и брендов\n")


@dp.callback_query(F.data == "HDPE_LDPE_canisters_typematerial")
async def HDPE_LDPE_canisters(callback: types.CallbackQuery):
    await callback.message.answer("Канистры ПНД, ПВД:\n\n"
                         "-Баллы за 1 килограмм: 5\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Всех размеров и цветов, в том числе от моторного масла")


@dp.callback_query(F.data == "LDPE_Stretch_film_typematerial")
async def LDPE_Stretch_film(callback: types.CallbackQuery):
    await callback.message.answer("Стретч-пленка ПВД:\n\n"
                         "-Баллы за 1 килограмм: 7\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Необходимо удалить скотч, наклейки\n"
                         "\t✅ Принимается отдельно от других видов пленки")


@dp.callback_query(F.data == "LDPE_film_typematerial")
async def LDPE_film(callback: types.CallbackQuery):
    await callback.message.answer("Пленка ПВД:\n\n"
                         "-Баллы за 1 килограмм: 7\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Необходимо удалить скотч, наклейки, срезать “застежки\n"
                         "\t✅ Плёнки можно сдавать вместе, не разделяя по видам")


@dp.callback_query(F.data == "HDPE_LDPE_PP_covers_typematerial")
async def HDPE_LDPE_PP_covers(callback: types.CallbackQuery):
    await callback.message.answer("Крышки ПНД, ПВД, ПП:\n\n"
                         "-Баллы за 1 килограмм: 15\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, cнять этикетки, вкладыши\n"
                         "\t✅ Только с маркировкой 2, 4, 5")


@dp.callback_query(F.data == "white_PET_bottles_from_drinks_typematerial")
async def white_PET_bottles_from_drinks(callback: types.CallbackQuery):
    await callback.message.answer("Белые ПЭТ-бутылки от напитков:\n\n"
                         "-Баллы за 1 килограмм: 5\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, cнять этикетки, вкладыши\n"
                         "\t✅ Только с маркировкой 2, 4, 5")


@dp.callback_query(F.data == "packing_packages_and_packagesTshirts_of_HDPE_LDPE_typematerial")
async def packing_packages_and_packagesTshirts_of_HDPE_LDPE(callback: types.CallbackQuery):
    await callback.message.answer("Пакеты фасовочные и пакеты-майки ПНД, ПВД:\n\n"
                         "-Баллы за 1 килограмм: 7\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Без скотча и наклеек")

@dp.callback_query(F.data == "PET_bottles_from_beverages_and_vegetable_oil_typematerial")
async def PET_bottles_from_beverages_and_vegetable_oil(callback: types.CallbackQuery):
    await callback.message.answer("ПЭТ-бутылки от напитков и растительного масла:\n\n"
                         "-Баллы за 1 килограмм: 5\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, спрессованные, с маркировкой\n"
                         "\t✅ Крышки необходимо откручивать и сдавать отдельно")


@dp.callback_query(F.data == "aluminum_cans_typematerial")
async def aluminum_cans(callback: types.CallbackQuery):
    await callback.message.answer("Алюминиевые банки:\n\n"
                         "-Баллы за 1 килограмм: 10\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, спресованные")



