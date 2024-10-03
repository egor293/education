def p(secs):
    hour=secs//3600
    min=(secs%3600)//60
    sec=secs%60
    return f'{hour:02d}:{min:02d}:{sec:02d}'
secs=int(input('seconds '))
print(p(secs))
