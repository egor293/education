black_list = ['j']
ochered=['a','g','j','k','x','n']
# for name in range(len(ochered)):
#     if len(ochered)==0:
#         break
#     else:
#         ochered.pop(0)
#         time+=1
#         print(ochered, time)
# print(time)

def queque(ochered,time=0):
    time-=len(black_list)
    while True:
        if len(ochered)==0:
            return time       
        ochered.pop(0)
        time+=1

print(queque(ochered))
