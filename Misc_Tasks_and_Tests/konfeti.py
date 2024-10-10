def pop(b,c):
    a=input('сколько конфет ').split()
    if len(a)<2:
        return(-1)
    for i in a:
        if int(i)>b:
            b=int(i)
    for i in a:
        i=int(i)
        c+=b-i     
    return c
print(pop(b=0,c=0))


    