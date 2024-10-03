def ass(a):
    max1=0
    cur=0
    for num in a:
        cur+=num
        max1=max(max1,cur)
    
        if cur<0:
            cur=0
    return max1
a=[-1,2,-3,-4,-5,-6,-7,1,2,3,4,56,6]
print(ass(a))        
        