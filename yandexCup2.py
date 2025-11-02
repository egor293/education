from math import log2, lcm

a, b, c = map(int, input().split())
n = int(input())

def f(x):
    ab = lcm(a, b)
    ac = lcm(a, c)
    bc = lcm(b, c)
    abc = lcm(a, b, c)
    number = (x // ab) + (x // ac) + (x // bc) - 3 * (x // abc)
    return number

def binary_search():
    LIMIT = 10 ** 18
    low = 0
    high = LIMIT
    for i in range(int(log2(LIMIT))):
        mid = (low + high) // 2
        fRes = f(mid)
        if fRes > LIMIT:
            return -1
        elif fRes == n:
            return mid
        elif fRes > n:
            low = high
        elif fRes < n:
            high = mid

    return -1


print(binary_search())
