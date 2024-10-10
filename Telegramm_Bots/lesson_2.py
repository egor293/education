from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import message

api_token='api token'
offset=0
bot=Bot(token=api_token)
url='https://api.telegram.org/bot'
dp=Dispatcher()

@dp.message(Command(commands=["start"]))
async def func_start(message):
    print(message)
    await message.answer(f"привет ты запустил бота")

@dp.message(Command(commands=["name"]))
async def func_id(message):
    await message.answer(f"ты написал {message.text}")
    

dp.run_polling(bot)
#. venv/Scripts/activate
