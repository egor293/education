#def score(dice):
#    total=0
#    for i in range(1,7):
#        if dice.count(i)>=3:
#            if i==1:
#                total+=i*1000
#            else:
#                total+=i*100
#            dice.remove(i)
#            dice.remove(i)
#            dice.remove(i)
#    for i in dice:
#        if i==1:
#            total+=100
#        elif i==5:
#            total+=50
#    return total
#dice=[5,1,3,4,1]
#print(score(dice))


def score(dice):
    total=0
    for i in range(1,7):
        count=dice.count(i)
        if count>=3:
            total+=1000*i if i==1 else 100*i
            count-=3
        total+=100*count if i==1 else 50 * count if i==5 else 0
    return total
dice=[5,1,3,4,1]
print(score(dice))
