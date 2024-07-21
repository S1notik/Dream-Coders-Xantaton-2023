import sqlite3
from aiogram import types, F
from aiogram.enums import ParseMode
from loader import dp

ranks = ["Новичок", "Опытный", "Ветеран", "Мастер", "Легенда"]


@dp.message(F.text == "Профиль👤")
async def education(message: types.Message):
    # con = sqlite3.connect("data/database/information_about_companies.db")
    # # Создание курсора
    # cur = con.cursor()
    # current_score = cur.execute("""SELECT score FROM users WHERE id = ?""", (str(message.from_user.id),)).fetchone()[0]
    # con.commit()
    # con.close()

    current_score = 1
    rank = ""

    if 0 <= current_score//100 <= 4:
        rank = ranks[0] + "👶"
    elif 5 <= current_score//100 <= 9:
        rank = ranks[1] + "👦"
    elif 10 <= current_score//100 <= 14:
        rank = ranks[2] + "👨"
    elif 15 <= current_score//100 <= 24:
        rank = ranks[3] + "🧔"
    else:
        rank = ranks[4] + "🧓"

    await message.answer("👤Ваш профиль:\n\n"
                         "🙂Имя: " + message.from_user.username + "\n"
                         "👑Ваше звание: " + rank + " в сортировке мусора♻️\n"
                         "🌟Ваш уровень: " + str(current_score//100) + "\n"
                         "✨Ващ текущий опыт: " + str(current_score%100) + "\\100" + " опыт\n",
                         parse_mode=ParseMode.HTML)


