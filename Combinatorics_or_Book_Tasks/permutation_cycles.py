# 1949
# 988
# 1147
# a=set([1,2,3,4,5,6,3,5,7,10,5,3])
# b=set([9,8,7,6,5,4,3,2,1])
# print(a)
# print(b)
# print(a.symmetric_difference(b))

from sympy import * 
print(sympy.combinatorics.permutations.Permutation.cycles([1,3,2]))  # type: ignore

def permutation_cycles(a):
    cycles=0
    s=0
    b=[]

    for i in a:
        a[i]==a[i]-1

    for i in a:
        if i in b:
            continue

        for i in range(len(a)):
            if a[a[i]]==i:
                cycles+=1
                break

        # if i==a[i-1]:
        #     cycles+=1
        #     continue    

        # if a[a[i-1]-1]==i:
        #     cycles+=1
        #     b.append(a[i-1])
        #     continue
            

        b.append(i)
    return cycles

a=[2,3,4,1]
print(permutation_cycles(a))
