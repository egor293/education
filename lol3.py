numbers = [1,2,3]
search=4

for number in numbers:
    if number == search:
        print('найдено')
        break
else:
    print('не найдено')


a = 8
b = 4
print('a,b')
a,b=b,a
print('a,b')


a = 3400
b = 2_342_344_343_4
print(type(a))
print(type(b))
print(type(a)==type(b))


#eval()
#exec()
a=3
b=eval('a+2')
print(b)
exec('c=a**2')
print(c)


print(bool(...))
print(bool(None))


a=[1,2,3]
a[0]=a
print(a[0])


a={'name':'Даниил','age':13}
a.update({'age':15,'status':'отличник'})
print(a)
print('status' in a)
print('second_name' in a)











