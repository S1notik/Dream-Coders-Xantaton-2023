from aiogram import Bot, types, Dispatcher
from data.config import token


bot = Bot(token=token, parse_mode="HTML")

dp = Dispatcher()