import requests

response = requests.get('http://www.sh-67.org.ru/')

if 'адрес' in response.text:
    print('есть')
else:
    print('нет')