def permutation_create(n,nums):
    nums1=list(range(1,n+1))
    a=0
    for i,item in enumerate(nums):
        if item in nums1:
            continue
        else:
            nums.pop(i)
            nums.insert(i,nums1[i])  
            a+=1 
    return nums,a
    
print(permutation_create(4,[1,6,9,4,2]))



