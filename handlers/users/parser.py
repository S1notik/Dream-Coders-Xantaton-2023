import csv
import requests
from aiogram import F, types

from keyboards.inline.inline_buttons import link_for_post_inline_keyboard
from loader import dp
import os

# all_posts = []
#
#
# def file_writer(all_posts):
#     with open("posts.csv", 'w') as file:
#         a_pen = csv.writer(file)
#         a_pen.writerow(("body", "url"))
#         for post in all_posts:
#             a_pen.writerow((post))
#
#
# file_writer(all_posts)



@dp.message(F.text == "Посты")
async def pars(message: types.Message):
    all_texts = []
    SECRET_TOKEN = str(os.getenv("SECRET_TOKEN"))
    version = 5.137
    domain = "eco4u2"
    count = 2
    offset = 1
    response = requests.get(
        "https://api.vk.com/method/wall.get",
        params={
            "access_token":  SECRET_TOKEN,
            "v": version,
            "domain": domain,
            "count": count,
            "offset": offset
        })
    data = response.json()
    for item in data['response']['items']:
        if item['post_type'] == 'post':
            await message.answer(item['text'],reply_markup=link_for_post_inline_keyboard)
