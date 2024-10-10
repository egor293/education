d={}
for idx,num in enumerate(nums):
    result=target-num
    if result in d:
        return [d]

