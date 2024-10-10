n=int(input())
a=0
b=1
i = 0
for _ in range(n):
    a, b = b, a+b
print(b)
    


