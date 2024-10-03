


year = int(input('введите год '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 and year % 100 != 0:
    print('високосный')
else:
    print('не високосный')

