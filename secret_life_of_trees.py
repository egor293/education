def secret_life_of_trees(trees):
    trees=sorted(trees)
    if trees[-1]-len(trees)+1<0:
        return 0
    if trees[0]>trees[-1]-len(trees)+1:
        return trees[-1]
        
    return trees[-1]-len(trees)+1

assert secret_life_of_trees([0,1,2,3,4,5,9])==3,secret_life_of_trees([0,1,2,3,4,5,9])
assert secret_life_of_trees([0,0,0,0,0,0,1])==0,secret_life_of_trees([0,0,0,0,0,0,1])
assert secret_life_of_trees([0,9])==8,secret_life_of_trees([0,9])
assert secret_life_of_trees([0,0])==0,secret_life_of_trees([0,0])
assert secret_life_of_trees([0,0,10000])==9998,secret_life_of_trees([0,0,10000])
assert secret_life_of_trees([7,4])==6,secret_life_of_trees([7,4])
assert secret_life_of_trees([5,5,5,5,5])==5,secret_life_of_trees([5,5,5,5,5])
assert secret_life_of_trees([4,5,5,5,5])==5,secret_life_of_trees([4,5,5,5,5])