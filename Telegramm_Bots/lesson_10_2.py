import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import message
import time,random

api_token='api token'
bot=Bot(token=api_token)
url1='https://api.telegram.org/bot'
dp=Dispatcher()

@dp.message(Command(commands=["start"]))
async def func_start(message):
    await message.answer(text="привет, напиши команду /help, чтобы узнать, что умеет этот бот.")

@dp.message(Command(commands=["help"]))
async def func_help(message):
    await message.answer(f"/help-возможности бота.\n"
                         f"/get_gif-бот отправит вам случайную гифку.")

@dp.message(Command(commands=["get_gif"]))
async def func_get_gif(message):
    response = requests.get('https://api.giphy.com/v1/gifs/random?api_key=j4MOYVqnS8FTR2FGNT8QoX72CKlFDSK8')
    await message.answer(response.json()['data']['images']['original']['url'])   

dp.run_polling(bot)





