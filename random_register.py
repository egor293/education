import random
fat=input()
a=''
for i in fat:
    if i.isalpha()==False:
        ...
    elif random.randint(1,3)==1:
        a+=i.upper()
    else:
        a+=i.lower()
print(a)
