cells=int(input())
cord_x=[]
cord_y=[]
for i in range(cells):
    x,y=map(int,input().split())
    cord_x.append(x)
    cord_y.append(y)
cord_x.sort()
cord_y.sort()
print(cord_x[0],cord_x[0],cord_x[-1],cord_x[-1])
