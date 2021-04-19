import requests
import json

base_url = 'https://www.dnd5eapi.co'

response = requests.get(base_url + '/api/spells/')

data = response.json()

test_response = requests.get('https://www.dnd5eapi.co/api/spells/acid-splash')
test_data = test_response.json()

def spell_entry(obj):
    data = obj
    count = 0
    for i in data['results']:
        spell = requests.get(base_url + i['url'])
        print(spell.json()['name'])
        classes = spell.json()['classes']
        for i in classes:
            print(i['name'])
        print(spell.json()['level'])
        print(spell.json()['desc'])
        count += 1
        if count >=5:
            break
    
spell_entry(data)









