def main(lst):
    array=[]
    zero=0
    for i in lst:
        if i!=0:
            array.append(i)
        else:
            zero+=1
    array.extend([0]*zero)
    return array,zero
lst=[1,0,1,2,0,1,3]
print(main(lst))
