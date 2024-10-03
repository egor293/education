# text=input('введите предложение ').lower()
# numbers=''
# words=text.split()
# #print(words)
# for word in words:
#     numbers+=str((words.index(word)))
# print(numbers)

words=input('введите предложение ').lower().split()
print(''.join(str((words.index(word))) for word in words))
