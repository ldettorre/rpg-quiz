import requests
import json


base_url = 'https://www.dnd5eapi.co'

response = requests.get(base_url + '/api/spells/')
data = response.json()

for i in data['results']:
    spell = requests.get(base_url + i['url'])
    print(spell.json()['name'])
    print(spell.json()['index'])
    print(spell.json()['desc'])
    


# print(base_url+individual_spell)




