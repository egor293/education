dict={0:['konstantin','gmail@gmail.com'],1:['krutoi','@@@@']}
b=0
print(dict)
while True:
    a=input()
    for key,element in dict.items():
        if a in element:
            print(dict[key][1])
            break
    if a not in dict[key]:
        dict[b]=[a,input('вас нет в списке, введите почту')]
    b+=1
    print(dict)

