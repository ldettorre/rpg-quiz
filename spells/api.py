import requests
import json
from .models import Spell


base_url = 'https://www.dnd5eapi.co'

response = requests.get(base_url + '/api/spells/')
data = response.json()

for i in data['results']:
    spell = requests.get(base_url + i['url'])
    print("Name:", spell.json()['name'])
    print("Index:", spell.json()['index'])
    print("Classes:", spell.json()['classes'])
    print("Level:", spell.json()['level'])
    print("Desc:", spell.json()['desc'])
    break
    
# name = "Burn"
# class_type = "Sorcerer"
# level = 5
# comical_description = "Do you smell toast"


# def spell_entry(name, class_type, level, comical_description):
#     s = Spell(name=name, class_type=class_type, level=level, points=level, comical_description=comical_description)
#     s.save()

# spell_entry(name, class_type, level, comical_description)





