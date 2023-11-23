from aiogram import types, F

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def parse(message: types.Message):
    print()