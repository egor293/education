import datetime
with open('zip_bomb.txt','r') as file:
    sorted_nums=list(map(int,file.read().split()))
a=9999798

def linear_search(sorted_nums,a):
    
    for idx,num in enumerate(sorted_nums):
        if a==num:return idx

def binary_search(sorted_nums,a):
    left=0
    right=len(sorted_nums)
    
    while left<=right:
        mid=(left+right)//2
        if mid==a:
            return mid
        elif mid<a:
            left=mid+1
        else:
            right=mid-1
    return -1


start=datetime.datetime.now()
print(linear_search(sorted_nums,a))
finish=datetime.datetime.now()
print(str(finish-start))

start=datetime.datetime.now()
print(binary_search(sorted_nums,a))
finish=datetime.datetime.now()
print(str(finish-start))

# nums=[i for i in range(1,100000000)]
# nums=list(map(str,nums))
# str_nums=' '.join(nums)
# with open('zip_bomb.txt','w') as file:
#     file.write(str_nums)
