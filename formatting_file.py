n=int(input())
answer=0
for i in range(n):
    space=int(input)
    answer+=space//4
    if space%4==1 or space%4==2:
        answer+=space%4
    elif space%4==3:
        answer+=2