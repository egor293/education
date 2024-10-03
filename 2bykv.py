name=input('Имя ')
a=[]
b=[name,]
for letter in name:
    a.append(letter)
while len(a)>2:
    if len(a)>2:
        a.pop(len(a)-1)
b.append(''.join(a))
if b[0]==b[1]:
    b.pop(0)
print(b)

    


