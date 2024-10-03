string=input('stroka ')
a=string.split()
b=dict()
for e in range(len(a)):
    c=1
    if a[e] in b:
        c+=1
        b[a[e]]=c
    else:
        b.setdefault(a[e], c)
print(b)
    
