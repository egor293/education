def main(price):
    banknotes={1:'Джордж Вашингтон',2:'Томас Джефферсон',5:'Авраам Линкольн',10:'Александр Гамильтон',20:'Эндрю Джексон',50:'Улисс Грант',100:'Бенджамин Франклин'}
    if price in banknotes:return banknotes[price]
    return 'wrong banknote price'

assert main(1)=='Джордж Вашингтон',main(1)
assert main(100)=='Бенджамин Франклин',main(1)
assert main(10000)=='wrong banknote price',main(10000)