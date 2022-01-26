import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from parseData import *
import time
import asyncio
import os

from aiogram.utils.markdown import hbold

import atslega

bot = Bot(token=atslega.tel_key, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

loop = asyncio.get_event_loop()
delay = 1000

#Need to put parse_all in the loop
@dp.message_handler(commands="loop")
async def my_func(message: types.Message):
    for i in range(10):
        time.sleep(delay)
        await message.answer("Looping")


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Ludza", "Rezekne"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Show the results in buffer", reply_markup=keyboard)


@dp.message_handler(Text(equals="Ludza"))
async def get_rez_Ludza(message: types.Message):
    await message.answer("Please Wait")

    # collect new ads
    parse_all()

    with open('data_temp.json', encoding='utf8') as json_file:
        dati = json.loads(json_file.read())

    for i in range(len(dati)):
        if dati[i]["regio"] == "ludza":
            card = f'{hbold(dati[i]["descr"])},\n' \
                   f'{hbold("Addres: ")}{dati[i]["address"]}\n' \
                   f'{hbold("Total prijs: ")}{dati[i]["totalPrice"]}\n' \
                   f'{hbold("Prijs per m2: ")}{dati[i]["price1m2"]}\n'

            await message.answer(card)


@dp.message_handler(Text(equals="Rezekne"))
async def get_rez_Ludza(message: types.Message):
    await message.answer("Please Wait")

    with open('data_temp.json', encoding='utf8') as json_file:
        dati = json.loads(json_file.read())

    for i in range(len(dati)):
        if dati[i]["regio"] == "rezekne":
            card = f'{hbold(dati[i]["descr"])},\n' \
                   f'{hbold("Addres: ")}{dati[i]["address"]}\n' \
                   f'{hbold("Total prijs: ")}{dati[i]["totalPrice"]}\n' \
                   f'{hbold("Prijs per m2: ")}{dati[i]["price1m2"]}\n'

            await message.answer(card)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()

