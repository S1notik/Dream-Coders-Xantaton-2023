from aiogram import types, F

from keyboards.inline.inline_buttons import infography_keyboard
from loader import dp


@dp.message(F.text == "Инфографика📑")
async def infografika(message: types.Message):
    text = message.text

    await message.answer("Инфографика - это то то")

@dp.message(F.text == "Батарейки")
async def bat(message: types.Message):
    await message.answer_photo("AgACAgIAAxkBAAPEZV4UbksK2D8JqkjISv0GfxGHjyMAAvzRMRvhWfFKEo1qNoy4V5YBAAMCAANzAAMzBA")



    '''if text == "Батарейки":
        await message.answer_photo("AgACAgIAAxkBAAPEZV4UbksK2D8JqkjISv0GfxGHjyMAAvzRMRvhWfFKEo1qNoy4V5YBAAMCAANzAAMzBA")
    elif text == "Композитная упаковка":
        await message.answer_photo("AgACAgIAAxkBAAPSZV4WlLjLAcdBTD1rgVJrNL1dhDoAAg7SMRvhWfFKzblwFjsP9pUBAAMCAANzAAMzBA")
    elif text == "Металл":
        await message.answer_photo("AgACAgIAAxkBAAPWZV4XPXa214zyQL2pz-io3jo5EdoAAhTSMRvhWfFKGNT50tu4XlMBAAMCAANzAAMzBA")
    elif text == "Пластик":
        await message.answer_photo("AgACAgIAAxkBAAPYZV4Xz6CCihsJT1TscsuOzHKkzlMAAhXSMRvhWfFKmZxSPBFCbx8BAAMCAANzAAMzBA")
    elif text == "Стекло":
        await message.answer_photo("AgACAgIAAxkBAAPaZV4YBuDHB8O4wRr15hUjSjukjosAAhjSMRvhWfFKtIZOrpWMF1kBAAMCAANzAAMzBA")
    elif text == "Экологичность упаковки":
        await message.answer_photo("AgACAgIAAxkBAAPcZV4YDU5ujdZCY4vk-7lAC3IIEEEAAhnSMRvhWfFKQEN4sBpwo4IBAAMCAANzAAMzBA")'''
