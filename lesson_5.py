# from aiogram import Bot, Dispatcher,F
# from aiogram.filters import Command
# from aiogram.types import Message,ReplyKeyboardRemove
# import time,random
# from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

# api_token='6933044019:AAEmapWcucHTO92tssbQMqcd9j9A5wwUVMY'
# bot=Bot(token=api_token)
# url='https://api.telegram.org/bot'
# dp=Dispatcher()
# button_1=KeyboardButton(text='sussy baka')
# button_2=KeyboardButton(text='skibidi toilet')


# keyboard_1=ReplyKeyboardMarkup(keyboard=[[button_1,button_2],[button_1,button_2]])

# @dp.message(Command(commands=["start"]))
# async def func_start(message):
#     await message.answer(text="s",reply_markup=keyboard_1)

# @dp.message(F.text.in_('sussy baka'))
# async def func_sussy_baka(message):
#     for i in range(10):
#         await message.answer(f"burger king!!!")

# @dp.message(F.text.in_('skibidi toilet'))
# async def func_skibidi_toilet(message):
#     for i in range(10):
#         await message.answer(f"KFC toilet!!!")







# dp.run_polling(bot)
#. venv/Scripts/activate