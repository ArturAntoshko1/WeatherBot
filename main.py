import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

from keyboards import main_keyboard
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
    await message.reply("хочешь ли ты получать информацию о погоде в своем городе?", reply_markup=main_keyboard())

# @dp.message_handler(Text(equals="Да, я хочу получать уведомления про погоду в своем городе"))
# async def save_user(message: types.Message) -> None:

if __name__ == "__main__":
    executor.start_polling(dp)