import json
import os

import requests
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

from weather import get_weather


load_dotenv()   

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def welcome(message: types.Message) -> None:
    await message.reply("пирвет пользователь! Отправь название города, в котором хочешь узнать погоду")
    

@dp.message_handler()
async def send_weather(message: types.Message) -> None:
    await message.reply(get_weather(message.text))


if __name__ == "__main__":
    executor.start_polling(dp)