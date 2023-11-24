import requests
from bs4 import BeautifulSoup as BS
from aiogram import F, types, Bot
from keyboards.inline import link_for_post_inline_keyboard
from loader import dp
import os
from lxml.etree import ParserError
from lxml import etree



@dp.message(F.text == "Посты")
async def pars(message: types.Message, bot: Bot):
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



'''@dp.message(F.text == "Посты")
async def pars(message: types.Message, bot: Bot):
    if message.from_user.id == 1649811196:
        url = "https://vk.com/eco4u2"
        response = requests.get(url).text
        soup = BS(response, features="html.parser")
        posts = soup.find(id="page_wall_posts")
        print(posts)
        html_doc = responce.content
        html_dom = parse_html_doc(html_doc)
        posts = html_dom.xpath("//*[@id=\"page_wall_posts\"]")
        print(len(posts))
        current_num_of_posts = 0

        #while True:


def parse_html_doc(html_doc):
    html_dom = None
    try:
        parser = etree.HTMLParser()
        html_dom = etree.HTML(html_doc, parser)
    except Exception as exception:
        print(exception)
    return html_dom


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
            await message.answer(item['text'], reply_markup=link_for_post_inline_keyboard)'''