def josephus(items,k):
    if len(items)==0:
        return []
    result=[]
    step=0
    for _ in range(len(items)):
        step=(step + k - 1)%len(items)
        items.append(items.pop(step))
    return result
items=[1,2,3,4,5,6,7]
k=3
josephus(items,k)