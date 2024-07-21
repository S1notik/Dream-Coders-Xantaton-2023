from aiogram import Bot, types, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from data import config


bot = Bot(token=config.token, parse_mode='HTML')

storage = MemoryStorage()

dp = Dispatcher(storage=storage)
