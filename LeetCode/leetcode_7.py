array=[1,1,3,2,2,2,3,3]
nums=[]
k=0
def zhopa(array):
    for i in array:
        if i not in nums:
            nums.append(i)
    for i in range(len(array)-len(nums)):  
        nums.append('_')
    k=len(nums)
    return (f'{k}, {nums}')
print(zhopa(array))
            

