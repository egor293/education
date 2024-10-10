import sys
b = int(input('введи ренж --- '))
a = [None] * b
count = 0
for i in range(b):
    a[i] = (sys.stdin.readline().rstrip())
print(*a)