queqe=[2,5,3,6,4]
position=1
time=0

for count in range(sum(queqe)):
    if queqe[0]>1:
        queqe.append(queqe.pop(0)-1)
    else:
        queqe.remove(1)
    time+=1
    position-=1
  


    
print(time)
