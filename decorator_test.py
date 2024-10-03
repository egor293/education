import time
def decorator(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print('время выполнения {} секунд'.format(end-start))
    return wrapper

@decorator
def sigma():
    for i in range(50000000):
        a=1+1
sigma()


