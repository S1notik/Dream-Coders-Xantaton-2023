from aiogram import types
from aiogram.filters import CommandStart
from aiogram import Bot, Dispatcher, F
from loader import dp


@dp.message(F.text == "Виды сырья🗑️")
async def types_mat(message: types.Message):
    await message.answer("В этом разжеле вы узнате о правилах приёма разлычных отходов")


@dp.callback_query(F.text == "Стеклянные бутылки и банки")
async def glass_bottle(callback: types.CallbackQuery):
    await callback.message.answer("Коричневые, зеленые и бесцветные стеклянные бутылки и банки:\n\n"
                         "-Баллы за 1 килограмм: 1\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, без крышек и ободков, бумажные этикетки можно не убирать\n"
                         "\t✅ Необходимо сдавать по отдельности коричневое, зеленое и бесцветное стекло")


@dp.callback_query(F.text == "Макулатура")
async def pwaste_papper(callback: types.CallbackQuery):
    await callback.message.answer("Макулатура:\n\n"
                         "-Баллы за 1 килограмм: 2\n\n"
                         "-Правила приема:\n"
                         "\t✅ Книги, газеты, журналы, бумага, гофрокартон\n"
                         "\t✅ Чистое, сложенное в коробки или перевязанное, без жирных пятен и остатков еды, без файлов и скрепок")


@dp.callback_query(F.text == "Пластиковые ящики ПНД")
async def plastic_box(callback: types.CallbackQuery):
    await callback.message.answer("Пластиковые ящики ПНД:\n\n"
                         "-Баллы за 1 килограмм: 5\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Всех размеров, цветов и толщины")


@dp.callback_query(F.text == "Батарейки")
async def batt(callback: types.CallbackQuery):
    await callback.message.answer("Батарейки:\n\n"
                        "-Баллы за 1 килограмм: 20\n\n"
                        "-Правила приема:\n"
                        "\t✅ Любых типов и брендов\n")


@dp.callback_query(F.text == "Канистры ПНД, ПВД")
async def kanistry(callback: types.CallbackQuery):
    await callback.message.answer("Канистры ПНД, ПВД:\n\n"
                         "-Баллы за 1 килограмм: 5\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Всех размеров и цветов, в том числе от моторного масла")


@dp.callback_query(F.text == "Стретч-пленка ПВД")
async def stretch_plenka(callback: types.CallbackQuery):
    await callback.message.answer("Стретч-пленка ПВД:\n\n"
                         "-Баллы за 1 килограмм: 7\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Необходимо удалить скотч, наклейки"
                         "\t✅ Принимается отдельно от других видов пленки")


@dp.callback_query(F.text == "Пленка ПВД")
async def plenka(callback: types.CallbackQuery):
    await callback.message.answer("Пленка ПВД:\n\n"
                         "-Баллы за 1 килограмм: 7\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Необходимо удалить скотч, наклейки, срезать “застежки”"
                         "\t✅ Плёнки можно сдавать вместе, не разделяя по видам")


@dp.callback_query(F.text == "Крышки ПНД, ПВД, ПП")
async def cap(callback: types.CallbackQuery):
    await callback.message.answer("Крышки ПНД, ПВД, ПП:\n\n"
                         "-Баллы за 1 килограмм: 15\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, cнять этикетки, вкладыши\n"
                         "\t✅ Только с маркировкой 2, 4, 5")


@dp.callback_query(F.text == "Белые ПЭТ-бутылки от напитков")
async def white_PAT_Bottle(callback: types.CallbackQuery):
    await callback.message.answer("Белые ПЭТ-бутылки от напитков:\n\n"
                         "-Баллы за 1 килограмм: 5\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, cнять этикетки, вкладыши\n"
                         "\t✅ Только с маркировкой 2, 4, 5")


@dp.callback_query(F.text == "Пакеты фасовочные и пакеты-майки ПНД, ПВД")
async def paking_and_tshirt_bags(callback: types.CallbackQuery):
    await callback.message.answer("Пакеты фасовочные и пакеты-майки ПНД, ПВД:\n\n"
                         "-Баллы за 1 килограмм: 7\n\n"
                         "-Правила приема:\n"
                         "\t✅ Чистые, без остатков еды, жира и других загрязнений\n"
                         "\t✅ Без скотча и наклеек")


