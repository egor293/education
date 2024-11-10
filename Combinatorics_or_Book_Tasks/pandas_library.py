import pandas

anime = pandas.read_csv('anime.csv')
# a=pandas.Series(['a','b','c','d'])
# print(a)
# print(a[1])
# print(a[1:])
# print(a[:1])

# dict={'sigma':[1,2,3],
#       'igma':[3,4,5],
#       'gma':[6,7,8],
#       'ma':[9,10,11],
#       'a':[12,13,14]}

# a=pandas.DataFrame(dict)
# print(a)
# a.index=('A','B','C')
# print(a)
# print(a['sigma'])
# print(a.tail(1))
# print(a.head(1))





print(anime)
print('|\n|\n|\n|\n|\n|\n|\n|\n')
print(anime[anime['rating']>=9.5])
print('|\n|\n|\n|\n|\n|\n|\n|\n')
print(anime[anime['rating']>=9.5])
print('|\n|\n|\n|\n|\n|\n|\n|\n')
print(anime[float(anime['episodes'])>=10000])
# print(anime['episodes'] > 1)