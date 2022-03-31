import requests

heroes = ['Hulk', 'Captain America', 'Thanos']
address = 'https://superheroapi.com/api/2619421814940190/search/'
result = {}
for hero in heroes:
    res = requests.get(address + hero)
    data = res.json()
    for i in data['results']:
        result[hero] = i['powerstats']

print(max(result, key = lambda k: int(result[k]['intelligence'])))
