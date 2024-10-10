import requests
token='token'
url='https://api.telegram.org/bot'
offset=0
result=requests.get(f'{url}{token}/getUpdates?offset={offset}').json()
print(result)
print(f"Вам написал {result['result'][0]['message']['from']['first_name']}")







































