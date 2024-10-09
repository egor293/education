def main(nums):
    answer={}
    for elem in nums:
        if elem in answer:
            answer[elem]+=1
            continue
        answer[elem]=1
    return answer

assert main([1,2,3,4,5,5,3,2,2,2])=={1:1,2:4,3:2,4:1,5:2},main([1,2,3,4,5,5,3,2,2,2])
assert main([-1,-1])=={-1:2},main([-1,-1])
assert main([0,0])=={0:2},main([0,0])

# from typing import Counter        
#   return(Counter(nums))
    

