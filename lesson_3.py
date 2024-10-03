from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import message
import time,random

api_token='6933044019:AAEmapWcucHTO92tssbQMqcd9j9A5wwUVMY'
offset=0
bot=Bot(token=api_token)
url='https://api.telegram.org/bot'
dp=Dispatcher()
user_ids={}

@dp.message(Command(commands=["start"]))
async def func_start(message):
    await message.answer(f"привет ты запустил бота")
    user_id=message.from_user.id
    if user_id not in user_ids:
        user_ids[user_id] = message.from_user.first_name
    print(user_ids)

@dp.message(Command(commands=["name"]))
async def func_id(message):
    await message.answer(f"твое имя {message.from_user.first_name}")

@dp.message(Command(commands=["id"]))
async def func_id(message):
    await message.answer(f"твой id {message.from_user.id}")

@dp.message(Command(commands=["help"]))
async def func_id(message):
    await message.answer(f"help-все команды бота")
    await message.answer(f"start-начать игру")
    await message.answer(f"bomber_jopa-запустить бомбер")
    await message.answer(f"name-узнать имя пользователя")
    await message.answer(f"id-узнать id пользователя")

@dp.message(Command(commands=["bomber_jopa"]))
async def func_bomber(message):
    # await message.answer(f"сколько раз тебе заспамить?)")
    for i in range(25):
        await message.reply(text=(str(random.randint(0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))))
        time.sleep(1)
dp.run_polling(bot)
#. venv/Scripts/activate
