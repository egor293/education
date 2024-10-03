import requests
search=input('введите запрос поиска гифок ')
response = requests.get('https://api.giphy.com/v1/gifs/search?api_key=j4MOYVqnS8FTR2FGNT8QoX72CKlFDSK8&q={search}&limit=1&offset=0&rating=r&lang=en&bundle=messaging_non_clips')

print(response.json()['data'][0]['url'])


# with open('12.gif', 'wb') as f:
#     f.write(response.content)
#     print(response.json()['data']['images']['original']['url'])