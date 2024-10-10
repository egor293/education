n=int(input())
array=map(int,input().split())
answer=[]
step='first'
for i in array:
    if step=='first':
        if i%2==0:
            answer.append('+')
    elif step=='second':
        if i%2!=0:
            answer.append('x')
        else:
            answer.append('+')
    elif step=='third':
        answer.append('x')
print(''.join(answer))