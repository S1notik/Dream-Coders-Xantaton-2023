from aiogram import types, F
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile

from keyboards.inline.inline_buttons import infography_keyboard
from loader import dp


@dp.message(F.text == "Инфографика📑")
async def infografika(message: types.Message):
    await message.answer("<b>В данном разделе вы можете узнать о переработке разных материалов</b>♻️",
                         reply_markup=infography_keyboard, parse_mode=ParseMode.HTML)


@dp.callback_query(F.data == "battery_infography")
async def battery(callback: types.CallbackQuery):
    await callback.message.answer_photo(FSInputFile("data/image/battery_infograf.png"))


@dp.callback_query(F.data == "paper_infography")
async def paper(callback: types.CallbackQuery):
    await callback.message.answer_photo(FSInputFile("data/image/paper_infograf.png"))


@dp.callback_query(F.data == "сomposite_package_infography")
async def сomposite_package(callback: types.CallbackQuery):
    await callback.message.answer_photo(FSInputFile("data/image/composite_pack_infograf.png"))


@dp.callback_query(F.data == "metal_infography")
async def metal(callback: types.CallbackQuery):
    await callback.message.answer_photo(FSInputFile("data/image/metal_infograf.png"))


@dp.callback_query(F.data == "plastic_infography")
async def plastic(callback: types.CallbackQuery):
    await callback.message.answer_photo(FSInputFile("data/image/plastic_infograf.png"))


@dp.callback_query(F.data == "glass_infography")
async def glass(callback: types.CallbackQuery):
    await callback.message.answer_photo(FSInputFile("data/image/glass_infograf.png"))


@dp.callback_query(F.data == "environmental_friendliness_of_packaging_infography")
async def environmental_friendliness_of_packaging(callback: types.CallbackQuery):
    await callback.message.answer_photo(FSInputFile("data/image/acolog_packaging_infograf.png"))


@dp.callback_query(F.data == "what_is_contain_bin_infography")
async def what_is_contain_bin(callback: types.CallbackQuery):
    await callback.message.answer_photo(FSInputFile("data/image/what_is_contain_bin_infography_infograf.jpg"))


@dp.callback_query(F.data == "responsible_consumption_infography")
async def responsible_consumption(callback: types.CallbackQuery):
    await callback.message.answer_photo(FSInputFile("data/image/responsible_consumption_infograf.jpg"))


