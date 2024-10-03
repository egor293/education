queue=[1, 6,1,1, 5]
position=3
a=queue[position]
time=0
b=0
while a in queue:
    if queue[0]>1:
        b=queue[0]
        queue.pop(0)
        queue.append(b)
        position=position-1
        time+=1
    else:
        b=queue[0]
        queue.pop(0)
        position=position-1
        time+=1
    if len(queue)==1 and queue[position]>0:
        break
    if position==-1:
        position+=len(queue)
    print(position)
    a=queue[position]    
print(time)

    


















# 1.создать перемные с входныи данными
# 2.узнать число билетов друга 
# 3.както полчить минуты