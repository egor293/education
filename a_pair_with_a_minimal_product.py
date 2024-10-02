def sigma(a):
    return min(a[0]*a[-1],a[-1]*a[-2],a[0]*a[1])

    # if a[0]<0 and a[-1]>0:
    #     return a[0]*a[-1]
    # elif a[0]<0 and a[0]<0:
    #     return a[-1]*a[-2]
    # else:
    #     return a[0]*a[1]
    
input()
a=list(map(int,input().split()))
a=sorted(a)   
print(sigma(a))

assert sigma([1,2,3,4] == 2)
assert sigma([-1,2,3,4] == -4)
assert sigma([1,2,3,4,5,6,7,8,9,0,-10,-19] == -171)


# assert (1*2)==2 , 'потому'
# assert (1*2)==3 , 'почему'
# assert 1*2==3 , 1*2