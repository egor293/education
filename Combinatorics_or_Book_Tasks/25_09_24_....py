set1={1,2,3,4,5,6,7,8}
set2={5,6,7,8,9,10,11,12}
list1=[1,2,3,4,5,6,7,8,9]
list2=[9,8,7,6,5,4,3,2,1]

print(set1)
set1.difference_update(set2)
print(set1) # удаляет все елементы из сета 1 в сете 2, возвращает None

print(set1.issuperset({1,2,3,4}))
print(set1.issuperset({1,2,3,4,5,6,7,9})) # проверяет содержит ли сет другой сет
print({1,2,3,4,5,6,7,8,9}.issuperset(set1))

print(set1.issubset({1,2,3,4,5,6,7,8}))
print(set1.issubset({1,2,3,4,5,6,7,8,9}))  # проверяет есть ли в одном сете все елементы другого
print(set1.issubset({9,8,7,6,5})) 

print(list1)
list1.extend(list1)
print(list1) # добавляет все елементы из одного списка/сета в другой через append, возвращает None
# list1.append(list2)
# print(list1)


print(set1)
print(set1.intersection(set2)) #???

set1.intersection_update #???

set1.isdisjoint #???

a=1
b=2
print('a={} b={}'.format(a,b))