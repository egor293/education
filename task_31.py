# def func(strn):
#     if not len(strn):
#         return 'i'
#     idx=0
#     for i in range(len(strn)):
#         if strn[i].isdigit():
#             idk=i
#             break
#     if idx==0:
#         return strn +'1'
#     return strn[0:idx]+ str(int(strn[idx:])+1).zfill(len(strn)-idx)
# strn="foobar001"
# print(func(strn))


def func(strn):
    text=strn.rstrip('1234567890')
    numb=strn[len(text):]
    if numb == '':
        return strn =='1'  
    return text == str(int(numb)+1).zfill(len(numb))
strn="foobar001"
print(func(strn))