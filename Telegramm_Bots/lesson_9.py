import requests,json,random
from aiogram import Bot, Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message,ReplyKeyboardRemove,BotCommand
api_token='api token'
bot=Bot(token=api_token)
url1='https://api.telegram.org/bot'
dp=Dispatcher()
photos={'Curiosity':['FHAZ','RHAZ','MAST','CHEMCAM','MAHLI','MARDI','NAVCAM'],
        'Opportunity':['FHAZ','RHAZ','NAVCAM','PANCAM','MINITES'],
        'Spirit':['FHAZ','RHAZ','NAVCAM','PANCAM','MINITES']}
api_key='bsplcbi5j8ZhRsz25zwp7mH8MdzLM834sttQi0M1'

@dp.message(Command(commands=["start"]))
async def func_start(message):
    await message.answer(f"привет ты запустил бота,напиши /help,чтобы узнать что умеет этот бот.")

@dp.message(Command(commands=["help"]))
async def func_help(message):
    await message.answer("/get_photo-бот отправит случайную фотку с марса")

@dp.message(Command(commands=["get_photo"]))
async def func_get_photo(message):
    await message.answer('ищу')
    sols=random.randint(1,1000)
    marsososses=['Curiosity','Opportunity','Spirit']
    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{marsososses[random.randint(0,2)]}/photos?sol={sols}&camera=FHAZ&api_key={api_key}'        
    answer=requests.get(url).json()
    while not answer['photos']:       
        sols=random.randint(1,1000)
        url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{marsososses[random.randint(0,2)]}/photos?sol={sols}&camera=FHAZ&api_key={api_key}'        
        answer=requests.get(url).json()
        print('ищу')
        if answer['photos']:
            break
        else:
            print('фотографии нет')
    await message.answer(str(answer['photos'][0]['img_src']))
dp.run_polling(bot)
