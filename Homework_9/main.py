import asyncio
import logging
from datetime import datetime
import time
from random import randint
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text

API_TOKEN = '5444000961:AAHOaRWOsYXkvs8ufgU9EvXJuxFKg-JK2xM'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def calculate(message: types.Message):
    res = message.text.split()
    if res[1] == '+':
        await message.answer(f'{res[0]} + {res[2]} = {int(res[0]) + int(res[2])}')
    if res[1] == '-':
        await message.answer(f'{res[0]} - {res[2]} = {int(res[0]) - int(res[2])}')
    if res[1] == '*':
        await message.answer(f'{res[0]} * {res[2]} = {int(res[0]) * int(res[2])}')
    if res[1] == '/':
        if res[2] == '0':
            await message.answer('Делить на 0 нельзя')
        else:
            await message.answer(f'{res[0]} / {res[2]} = {int(res[0]) / int(res[2])}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)