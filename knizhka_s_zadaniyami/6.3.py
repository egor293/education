# a=list(map(int,input().split()))
def count(a):
    while True:
        result=0
        max2=max(a)
        min2=min(a)
        if max2>=20 and min2>=10:
            a[a.index(max2)]=max2-20
            a[a.index(min2)]=min2-10
            result+=1
        else:
            return result
        
assert count([41,80])==4, count([41,80])
assert count([100,90])==6, count([100,90])
assert count([0,20])==0, count([0,20])
assert count([0,60])==0, count([0,60])
assert count([20,120])==1, count([20,120])


            