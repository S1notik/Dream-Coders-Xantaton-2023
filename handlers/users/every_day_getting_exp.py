import sqlite3
import time
from aiogram import types, F
import datetime
from loader import dp
import aioschedule
import asyncio


'''@dp.message(F.text == "activate_daily")
async def pars(message: types.Message):
    while True:
        print()'''

#
# @dp.message(F.text == "Забрать опыт✨️")
# async def taking_daily(message: types.Message):
#     con = sqlite3.connect("data/database/information_about_companies.db")
#     # Создание курсора
#     cur = con.cursor()
#     is_daily_exp_was_got = cur.execute("""SELECT daily FROM users WHERE id = ?""", (message.from_user.id,)).fetchone()[0]
#
#     if is_daily_exp_was_got != True:
#         # Здесь прсчитывается тест, но я уже в душе не чаю зачем
#         #await score_for_questions(message.from_user.id)
#         cur.execute(f"""UPDATE users SET daily={True} WHERE id={message.from_user.id}""")
#         await message.answer("✅Вы получали 10 опыта!")
#         await timer(message.from_user.id)
#     else:
#         await message.answer("❌Вы уже получали сегодня опыт!")
#
#     con.commit()
#     con.close()
#
# async def timer(user_id):
#     time.sleep(10)
#     con = sqlite3.connect("data/database/information_about_companies.db")
#     # Создание курсора
#     cur = con.cursor()
#     cur.execute(f"""UPDATE users SET daily={False} WHERE id={user_id}""")
#     con.commit()
#     con.close()


'''taked = False
@dp.callback_query(F.data == "take_exp")
async def take_exp(callback: types.CallbackQuery):
    global taked
    if not taked:
        await score_for_questions(callback.message.from_user.id)
        taked = True
    else:
        await callback.message.answer("❌Вы уже получали сегодня опыт!")

async def take_exp(message: types.Message):
    await message.answer("Не забудьте забрать ежедневную exp✨", reply_markup=take_exp_keyboard)
    taked = False


async def scheduler():
    aioschedule.every().day.at("2:35").do(take_exp)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(dp):
    asyncio.create_task(scheduler())'''