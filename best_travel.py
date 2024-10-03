from itertools import combinations,product,permutations

# e1=product('ABCD')
# print(list(e1))

# e2=product('ABCD',[1,2])
# print(list(e2))

# e3=product('ABCD',[1,2],[3,4],[5,6])
# print(list(e3))

# e1=permutations('ABC')
# print(list(e1))

# e2=permutations([1,2,3],2)
# print(list(e2))

# e1=combinations('ABC',2)
# print(list(e1))   

def choose_best_sum(t,k,ls):
    result=0
    for combination in combinations(ls,k):
        s=sum(combination)
        if s<=t and s>result:
        result=s
    if result==0:
        return None
    return result