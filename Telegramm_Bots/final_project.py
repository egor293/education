from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import message
from dadata import Dadata
import requests

api_token='api token'
token = "token"
dadata = Dadata(token)
offset=0
bot=Bot(token=api_token)
url='https://api.telegram.org/bot'
dp=Dispatcher()
url1='https://api.ipgeolocation.io/ipgeo?apiKey=0fd544a9c1724ffb84b9998d444a7832&ip=5.167.120.0&lang=ru'


@dp.message(Command(commands=["start"]))
async def func_start(message):
    await message.answer(f"привет ты запустил бота,напиши /help,чтобы узнать что умеет этот бот.")

@dp.message(Command(commands=["help"]))
async def func_help(message):
    await message.answer(f"/ip_get-узнать адрес по ip")

@dp.message(Command(commands=["ip_get"]))
async def func_ip_get(message):
    await message.answer('отправьте ip адрес')

@dp.message()
async def ip_request(message):
    if dadata.iplocate(message.text)=={"location": ...}:
        await message.answer('ip адрес не действителен пожалуйста отправьте верный адрес')
    else:
        result=dadata.iplocate(str(message.text))
        print(result)
        await message.answer(f"страна-{result['data']['country']} \n"
                             f"область/край/регион-{result['data']['region_with_type']} \n"
                             f"город/село-{result['value']} \n"
                             f"широта-{result['data']['geo_lat']} \n"
                             f"долгота-{result['data']['geo_lon']} ")
    print(dadata.iplocate('5.167.120.0'))
# print(requests.get(url1).json)

dp.run_polling(bot)
