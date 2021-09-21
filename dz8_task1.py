import requests

super_hero_id = []
super_hero_list = []
m = []

super_hero_name = ['Hulk', 'Captain America', 'Thanos']
for i in super_hero_name:
    url = 'https://superheroapi.com/api/2619421814940190/search/%s/'
    resp = requests.get(url % i)
    pers = resp.json()
    result = pers["results"][0]
    super_hero_id.append(result['id'])

for i in super_hero_id:
    url = 'https://superheroapi.com/api/2619421814940190/%s/powerstats/'
    resp = requests.get(url % i)
    stats = {}
    stats['name'] = resp.json()['name']
    stats['intelligence'] = resp.json()['intelligence']
    super_hero_list.append(stats)

for el in super_hero_list:
    el = int(el['intelligence'])
    m.append(el)
m.sort()
intelligent_max = m[-1]

for el in super_hero_list:
    for v in el:
        if el['intelligence'] == str(intelligent_max):
            smart = el['name']

print(f"Самый умный: {smart}")
