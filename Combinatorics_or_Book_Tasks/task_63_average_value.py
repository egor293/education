def main(nums):
    if nums[0]==0:
        return 'error'
    a=0
    for i,num in enumerate(nums):
        if num!=0:
            a+=num
            continue
        return a/len(nums[:i])

assert(main(nums=[1,2,3,4,0]))==2.5,main(nums=[1,2,3,4,0])
assert(main(nums=[0,2,3,4,0]))=='error',main(nums=[0,2,3,4,0])
assert(main(nums=[1,2,3,4,0,5]))==2.5,main(nums=[1,2,3,4,0,5])