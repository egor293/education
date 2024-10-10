from aiogram import Bot, Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message,ReplyKeyboardRemove,BotCommand
import time,random
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
import requests

url='https://jsonplaceholder.typicode.com/todos'
offset=0
texts=requests.get(url).json()

api_token='api token'
bot=Bot(token=api_token)
url1='https://api.telegram.org/bot'
dp=Dispatcher()

async def asrock(bot):
    main_menu_commands=[
        BotCommand(command='/help',description='помощь'),
        BotCommand(command='/lat',description='латинская фраза')]
    await bot.set_my_commands(main_menu_commands)

@dp.message(Command(commands=["start"]))
async def func_start(message):
    await message.answer(f"привет ты запустил бота,напиши /help,чтобы узнать что умеет этот бот.")

@dp.message(Command(commands=["help"]))
async def func_help(message):
    await message.answer("/lat-бот отправит случайную латинскую фразу")

@dp.message(Command(commands=["lat"]))
async def func_lat(message):
    await message.answer(texts[random.randint(1,len(texts))]['title'])

dp.startup.register(asrock)
dp.run_polling(bot)
