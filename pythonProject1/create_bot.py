from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

create_bot = Bot(token=os.getenv('5444000961:AAHOaRWOsYXkvs8ufgU9EvXJuxFKg-JK2xM'))
dp = Dispatcher(create_bot)