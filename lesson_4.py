from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import message
import time,random

api_token='6933044019:AAEmapWcucHTO92tssbQMqcd9j9A5wwUVMY'
offset=0
bot=Bot(token=api_token)
url='https://api.telegram.org/bot'
dp=Dispatcher()
users={}



@dp.message(Command(commands=["start"]))
async def func_start(message):
    await message.answer(f"привет ты запустил бота,напиши /help,чтобы узнать что умеет этот бот.")
    user=message.from_user.id
    if user not in users:
        users[user] = {'number': 1,
                       'attempts': 3,
                       'MAX_NUMBER':10,
                       'wins':0,
                       'games':0,
                       'defeats':0,
                       'game_state':False,
                       'difficulty_change_state':False,
                       'attempts_change_state':False}
                    
    print(users)

@dp.message(Command(commands=["name"]))
async def func_name(message):
    await message.answer(f"твое имя {message.from_user.first_name}.")

@dp.message(Command(commands=["id"]))
async def func_id(message):
    await message.answer(f"твой id {message.from_user.id}.")

@dp.message(Command(commands=["help"]))
async def func_help(message):
    await message.answer(f"/help-все команды бота.\n"
                         f"/start-запустить бота.\n"
                         f"/bomber_jopa-запустить бомбер.\n"
                         f"/name-узнать имя пользователя.\n"
                         f"/id-узнать id пользователя.\n"
                         f"/play-начать игру.\n"
                         f"/game_rules-узнать правила игры.\n"
                         f"/game_level_of_difficulty-указать сложность игры.\n"
                         f"/game_attempts-указать количество попыто на игру.\n"
                         f"/stats-узнать статистику пользователя.\n")
    
@dp.message(Command(commands="stats"))
async def func_stats(message):
    await message.answer(f"количество побед: {users[message.from_user.id]['wins']}.\n"
                         f"количество поражений: {users[message.from_user.id]['defeats']}.\n"
                         f"количество игр: {users[message.from_user.id]['games']}.\n")
@dp.message(Command(commands=["bomber_jopa"]))
async def func_bomber_jopa(message):
    for i in range(25):
        await message.reply(text=(str(random.randint(0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))))
        time.sleep(1)

@dp.message(Command(commands=["play"]))
async def func_play(message):
    users[message.from_user.id]['game_state']=True
    await message.answer(f'я загадал число от 1 до {users[message.from_user.id]['MAX_NUMBER']},попробуй угадать.'
                         f'у вас {users[message.from_user.id]['attempts']}  попыток.')
    users[message.from_user.id]['number']=random.randint(1,users[message.from_user.id]['MAX_NUMBER'])
    print(users)

@dp.message(Command(commands=["game_rules"]))
async def func_game_rules(message):
    await message.answer(f'правила игры:\n'
                         f'бот загадает случайное число в дапазоне который вы можете указать с поммощью команды /game_level_of_difficulty.\n'
                         f'стандартная сложность от 1 до 10 и 3 попытки.')
    
@dp.message(Command(commands=["game_attempts"]))
async def func_game_attempts(message):
    users[message.from_user.id]['attempts_change_state']=True
    await message.answer(f'напишите количество попыток,на эту игру.')
   
    
@dp.message(Command(commands=["game_level_of_difficulty"]))
async def func_game_level_of_difficulty(message):
    users[message.from_user.id]['difficulty_change_state']=True
    await message.answer(f'напишите максимальное число,которое сможет загадать бот.\n'
                         f'поправка,от 1 до указанного числа.')
    
    
@dp.message()
async def game(message):
        if users[message.from_user.id]['game_state']==True:
            if int(message.text)>users[message.from_user.id]['number']:
                users[message.from_user.id]['attempts']-=1
                await message.answer(f'неверно,число меньше.\nУ вас осталолсь {users[message.from_user.id]['attempts']} попыток.')                
            elif int(message.text)<users[message.from_user.id]['number']:
                users[message.from_user.id]['attempts']-=1
                await message.answer(f'неверно,число больше.\nУ вас осталолсь {users[message.from_user.id]['attempts']} попыток.')                
            elif int(message.text)==users[message.from_user.id]['number']:
                await message.answer('верно,ты победил.') 
                users[message.from_user.id]['wins']+=1
                users[message.from_user.id]['attempts']=3
                users[message.from_user.id]['game_state']=False
            elif int(message.text)>users[message.from_user.id]['MAX_NUMBER'] or int(message.text)<users[message.from_user.id]['MAX_NUMBER']:
                await message.answer(f'число вне дапазона.\n'
                                     f'напиште число от 1 до {users[message.from_user.id]['MAX_NUMBER']}.')
            if users[message.from_user.id]['attempts']==0:
                await message.answer('попытки кончились,вы проиграли.')
                users[message.from_user.id]['attempts']=3
                users[message.from_user.id]['defeats']+=1
                users[message.from_user.id]['game_state']=False
        if users[message.from_user.id]['attempts_change_state']==True:
            users[message.from_user.id]['attempts']=int(message.text)
            users[message.from_user.id]['attempts_change_state']=False
            await message.answer(f'количество попыток установлено на {users[message.from_user.id]['attempts']}.')
        if users[message.from_user.id]['difficulty_change_state']==True:
            users[message.from_user.id]['MAX_NUMBER']=int(message.text)
            users[message.from_user.id]['difficulty_change_state']=False
            await message.answer(f'количество максимальное число,которые бот сможет загадать установлено на значение {users[message.from_user.id]['MAX_NUMBER']}.')
        elif users[message.from_user.id]['attempts_change_state']==False and users[message.from_user.id]['difficulty_change_state']==False and users[message.from_user.id]['game_state']==False:
            await message.answer('вы не в игре')

dp.run_polling(bot)
#. venv/Scripts/activate
