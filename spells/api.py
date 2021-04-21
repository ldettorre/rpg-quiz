import requests
import json
from .models import ClassType, Spell


base_url = 'https://www.dnd5eapi.co'

response = requests.get(base_url + '/api/spells/')

data = response.json()

def spell_entry(obj):
    data = obj

    for i in data['results']:
        spell = requests.get(base_url + i['url'])
        spell_name = spell.json()['name']
        spell_classes = spell.json()['classes']
        
        new_classes =[]
        for i in spell_classes:
            class_type = i['name']
            existing_classes = ClassType.objects.all()
            for e in existing_classes:
                if class_type == e.name:
                    new_classes.append(e.id)
        
        spell_level = spell.json()['level']
        spell_desc = spell.json()['desc']
        spell_universe = "D&D"
    
        spell = Spell.objects.create(name=spell_name, 
            level=spell_level, 
            points=spell_level, 
            comical_description=spell_desc, 
            fantasy_universe=spell_universe)
        for i in new_classes:
            spell.class_type.add(i)
    

    
spell_entry(data)

# Below loops over the API classes and creates them within our db.

# base_url = 'https://www.dnd5eapi.co'

# response = requests.get(base_url + '/api/classes/')

# data = response.json()

# for d in data['results']:
#     new_class = d['name']
#     ClassType.objects.create(name=new_class)







