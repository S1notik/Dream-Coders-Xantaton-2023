from aiogram import types, F
from loader import dp


@dp.message(F.text)
async def infografika(message: types.Message):
    if message.text == "Батарейки":
        await message.answer_photo("AgACAgIAAxkBAAPEZV4UbksK2D8JqkjISv0GfxGHjyMAAvzRMRvhWfFKEo1qNoy4V5YBAAMCAANzAAMzBA")
    elif message.text == "Композитная упаковка":
        await message.answer_photo("AgACAgIAAxkBAAPSZV4WlLjLAcdBTD1rgVJrNL1dhDoAAg7SMRvhWfFKzblwFjsP9pUBAAMCAANzAAMzBA")
    elif message.text == "Металл":
        await message.answer_photo("AgACAgIAAxkBAAPWZV4XPXa214zyQL2pz-io3jo5EdoAAhTSMRvhWfFKGNT50tu4XlMBAAMCAANzAAMzBA")
    elif message.text == "Пластик":
        await message.answer_photo("AgACAgIAAxkBAAPYZV4Xz6CCihsJT1TscsuOzHKkzlMAAhXSMRvhWfFKmZxSPBFCbx8BAAMCAANzAAMzBA")
    elif message.text == "Стекло":
        await message.answer_photo("AgACAgIAAxkBAAPaZV4YBuDHB8O4wRr15hUjSjukjosAAhjSMRvhWfFKtIZOrpWMF1kBAAMCAANzAAMzBA")
    elif message.text == "Экологичность упаковки":
        await message.answer_photo("AgACAgIAAxkBAAPcZV4YDU5ujdZCY4vk-7lAC3IIEEEAAhnSMRvhWfFKQEN4sBpwo4IBAAMCAANzAAMzBA")
