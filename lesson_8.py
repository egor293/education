import requests,json,random
photos={'Curiosity':['FHAZ','RHAZ','MAST','CHEMCAM','MAHLI','MARDI','NAVCAM'],
        'Opportunity':['FHAZ','RHAZ','NAVCAM','PANCAM','MINITES'],
        'Spirit':['FHAZ','RHAZ','NAVCAM','PANCAM','MINITES']}
api_key='bsplcbi5j8ZhRsz25zwp7mH8MdzLM834sttQi0M1'
def sus(photos,api_key):
    sols=random.randint(1,1000)
    marsososses=['Curiosity','Opportunity','Spirit']
    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{marsososses[random.randint(0,2)]}/photos?sol={sols}&camera=FHAZ&api_key={api_key}'        
    answer=requests.get(url).json()
    while not answer['photos']:       
        url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{marsososses[random.randint(0,2)]}/photos?sol={sols}&camera=FHAZ&api_key={api_key}'        
        answer=requests.get(url).json()
        if answer['photos']:
            return answer['photos'][0]['img_src']
        else:
            print('фотографии нет')
print(sus(photos,api_key))

