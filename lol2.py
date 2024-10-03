a = input().split()
b=0
c=True
for i in a:
    if i == 'flick':
        c=not c
        a[b]=c
        b+=1
    else:
        a[b]=c
        b+=1
print(a)

