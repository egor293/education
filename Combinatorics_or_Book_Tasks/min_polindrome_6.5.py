import test_min_palindrom
from typing import Counter

def polindrome(pol):
    a=Counter(pol)
    pol=sorted(list(set(pol)))
    min_pol=[]
    b=False
    i=0
    for _ in range(len(pol)):
        if a[pol[_]]>=2:
            min_pol.insert(i,pol[_]*(a[pol[_]]//2))
            min_pol.insert(-(i+1),pol[_]*(a[pol[_]]//2))
            i+=1
        if b==False and a[pol[_]]%2!=0:
            c=pol[_]
            b=True    
    if b==True:   
        min_pol.insert(len(min_pol)//2,c)
    return ''.join(min_pol)

test_min_palindrom.start_test(polindrome)