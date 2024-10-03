import requests
token='6418350421:AAEYsvS7iM1Ggz8gxJhakA0P5uoAvx15JuM'
url='https://api.telegram.org/bot'
offset=0
result=requests.get(f'{url}{token}/getUpdates?offset={offset}').json()
print(result)
print(f"Вам написал {result['result'][0]['message']['from']['first_name']}")
'6785442606:AAG6XOf9CjMKyJ6MnBiF7OoTeii0OKplEkY' #токен тимофея






































