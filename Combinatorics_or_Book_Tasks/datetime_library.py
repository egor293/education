import datetime
import time
# def count(start,end):
#     return end-start

# def main():
#     data=list(map(int,input().split()))
#     return count(start=data[0],end=data[1])

# print(main())

# time=datetime.datetime.now()
# months={1:'января',2:'февраля',3:'марта',4:'апреля',5:'мая',6:'июня',7:'июля',8:'августа',9:'сентября',10:'октября',11:'ноября',12:'декабря'}
# print(f'Сегодня {time.day} {months[time.month]} {time.year} года.Время {time.hour} часов {time.minute} минут {time.second} секунд')


# def timer(seconds):
#     print(datetime.datetime.now())
#     time.sleep(seconds)
#     return datetime.datetime.now()

# seconds=int(input('количество секунд '))
# print(timer(seconds))



def count(start,end,holidays):
    count=0
    for i in holidays:
        if i>start and i<end:
            count-=1
    while start<end:
        if start.weekday()>6:
            continue
        start+=datetime.timedelta(1)
        count+=1
    return count



start=datetime.datetime.strptime(input(),'%d.%m.%Y').date()
end=datetime.datetime.strptime(input(),'%d.%m.%Y').date()
holidays=list(map(str,input().split()))
for i,elem in enumerate(holidays):
    holidays.pop(i)
    holidays.insert(i,datetime.datetime.strptime(elem,'%d.%m.%Y').date())
print(count(start,end,holidays))