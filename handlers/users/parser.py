import requests
from bs4 import BeautifulSoup as BS
from aiogram import F, types
from keyboards.inline import link_for_post_inline_keyboard
from loader import dp
import os


@dp.message(F.text == "Посты")
async def pars(message: types.Message):
    request = requests.get("https://vk.com/eco4u2")
    html = BS(request.content, "html.parser")
    posts = html.select("//*[@id=\"page_wall_posts\"]")
    current_num_of_posts = 0
    if message.from_user.id == 1649811196:
        while True:
            request = requests.get("https://vk.com/eco4u2")
            html = BS(request.content, "html.parser")



async def send_post_to_telegram(message: types.Message):
    SECRET_TOKEN = str(os.getenv("SECRET_TOKEN"))
    version = 5.137
    domain = "eco4u2"
    count = 1
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
            await message.answer(item['text'], reply_markup=link_for_post_inline_keyboard)