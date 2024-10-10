import requests

url='https://jsonplaceholder.typicode.com/todos'
offset=0
h=requests.get(url).json()
a=0
for i in range(100):
    print(h[a]['title'])
    a+=1