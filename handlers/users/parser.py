import requests
from aiogram import F, types
from loader import dp
import os


@dp.message(F.text == "Посты")
async def pars(message: types.Message):
    SECRET_TOKEN = str(os.getenv("SECRET_TOKEN"))
    version = 5.137
    domain = "eco4u2"
    count = 2
    offset = 1
    response = requests.get(
        "https://api.vk.com/method/wall.get",
        params={
            "access_token": SECRET_TOKEN,
            "v": version,
            "domain": domain,
            "count": count,
            "offset": offset
        })
    data = response.json()
    for item in data['response']['items']:
        if item['post_type'] == 'post':
            await message.answer(item['text'])
