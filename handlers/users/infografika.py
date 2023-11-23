from aiogram import types, F

from keyboards.inline.inline_buttons import get_infography_keyboard, infography_builder
from loader import dp


@dp.message(F.text == "Инфографика📑")
async def infografika(message: types.Message):
    await message.answer("Здесь вы можете узнать о переработке разных материалов", reply_markup=infography_builder.as_markup())

@dp.callback_query(F.data == "battery_infography")
async def battery(callback: types.CallbackQuery):
    await callback.message.answer_photo("AgACAgIAAxkBAAPEZV4UbksK2D8JqkjISv0GfxGHjyMAAvzRMRvhWfFKEo1qNoy4V5YBAAMCAANzAAMzBA")

@dp.callback_query(F.data == "сomposite_package_infography")
async def сomposite_package(callback: types.CallbackQuery):
    await callback.message.answer_photo("AgACAgIAAxkBAAPSZV4WlLjLAcdBTD1rgVJrNL1dhDoAAg7SMRvhWfFKzblwFjsP9pUBAAMCAANzAAMzBA")

@dp.callback_query(F.data == "metal_infography")
async def metal(callback: types.CallbackQuery):
    await callback.message.answer_photo("AgACAgIAAxkBAAPWZV4XPXa214zyQL2pz-io3jo5EdoAAhTSMRvhWfFKGNT50tu4XlMBAAMCAANzAAMzBA")

@dp.callback_query(F.data == "plastic_infography")
async def plastic(callback: types.CallbackQuery):
    await callback.message.answer_photo("AgACAgIAAxkBAAPYZV4Xz6CCihsJT1TscsuOzHKkzlMAAhXSMRvhWfFKmZxSPBFCbx8BAAMCAANzAAMzBA")

@dp.callback_query(F.data == "glass_infography")
async def glass(callback: types.CallbackQuery):
    await callback.message.answer_photo("AgACAgIAAxkBAAPaZV4YBuDHB8O4wRr15hUjSjukjosAAhjSMRvhWfFKtIZOrpWMF1kBAAMCAANzAAMzBA")

@dp.callback_query(F.data == "environmental_friendliness_of_packaging_infography")
async def environmental_friendliness_of_packaging(callback: types.CallbackQuery):
    await callback.message.answer_photo("AgACAgIAAxkBAAPcZV4YDU5ujdZCY4vk-7lAC3IIEEEAAhnSMRvhWfFKQEN4sBpwo4IBAAMCAANzAAMzBA")



'''
@dp.callback_query(F.data == "paper_infography")
async def paper(callback: types.CallbackQuery):
    await callback.message.answer_photo("AgACAgIAAxkBAAOkZV7NLDIt692t4wre8yXQjGLuM0EAAqPXMRvu6fBKcc_TTR3SeocBAAMCAANzAAMzBA")

@dp.callback_query(F.data == "what_is_contain_bin_infography")
async def what_is_contain_bin(callback: types.CallbackQuery):
    await callback.message.answer_photo("AgACAgIAAxkBAAOxZV7R2KH7GmHgIP_sZi73HfHauSIAAq3XMRvu6fBKcMo08NIstu4BAAMCAANzAAMzBA")

@dp.callback_query(F.data == "responsible_consumption_infography")
async def responsible_consumption(callback: types.CallbackQuery):
    await callback.message.answer_photo("AgACAgIAAxkBAAOcZV7FhX9GKPaoAuEJKjwfyt2JbkYAApzXMRvu6fBKhfq0gE1coEMBAAMCAANzAAMzBA")
'''

