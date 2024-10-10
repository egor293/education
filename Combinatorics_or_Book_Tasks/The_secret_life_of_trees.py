def The_secret_life_of_trees(n,list):
    if len(list)==1: return list[0]
    list=sorted(list)
    count=0
    for item in list:
        if list[-1]>item:
            count+=1
    if list[-1]>len(list):
        count-=list[-1]-n+1
    return n-1-count

# n=int(input())
# list=sorted(list(map(int,input().split())))

assert The_secret_life_of_trees(n=4,list=[0,0,3,3])==1 , The_secret_life_of_trees(n=4,list=[0,0,3,3])
assert The_secret_life_of_trees(n=3,list=[2,0,1])==0 , The_secret_life_of_trees(n=3,list=[2,0,1])
assert The_secret_life_of_trees(n=1,list=[2])==2 , The_secret_life_of_trees(n=1,list=[2])
assert The_secret_life_of_trees(n=2,list=[0,4])==3 , The_secret_life_of_trees(n=1,list=[0,4])
assert The_secret_life_of_trees(n=2,list=[0,9])==8 , The_secret_life_of_trees(n=2,list=[0,9])
assert The_secret_life_of_trees(n=2,list=[0,52])==51 , The_secret_life_of_trees(n=2,list=[0,52])
assert The_secret_life_of_trees(n=5,list=[0,52,1,4,6])==48, The_secret_life_of_trees(n=5,list=[0,52,1,4,6])




        


