from aiogram import Bot, Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message,ReplyKeyboardRemove,BotCommand
import time,random
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

api_token='6933044019:AAEmapWcucHTO92tssbQMqcd9j9A5wwUVMY'
bot=Bot(token=api_token)
url='https://api.telegram.org/bot'
dp=Dispatcher()

async def asrock(bot):
    main_menu_commands=[
        BotCommand(command='/sus',description='amogus'),
        BotCommand(command='/sus',description='amogus111'),
        BotCommand(command='/sus',description='amogus11'),
        BotCommand(command='/sus',description='amogus1')]
    await bot.set_my_commands(main_menu_commands)
    
@dp.message(Command(commands=["sus"]))
async def func_sus(message):
    await message.answer(text='momogus')

@dp.message(Command(commands=["start"]))
async def func_start(message):
    await message.answer(text="watafak?")
    
dp.startup.register(asrock)
dp.run_polling(bot)
