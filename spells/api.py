import requests
import json
from .models import ClassType


base_url = 'https://www.dnd5eapi.co'

response = requests.get(base_url + '/api/spells/')

data = response.json()

def spell_entry(obj):
    data = obj
    count = 0
    for i in data['results']:
        spell = requests.get(base_url + i['url'])
        # name = spell.json()['name']
        classes = spell.json()['classes']
        for i in classes:
            class_type = i['name']
            print(class_type, type(class_type))
            existing_classes = ClassType.objects.all()
            for e in existing_classes:
                if class_type == e.name:
                    print("Match")
        # level = spell.json()['level']
        # comical_description = spell.json()['desc']
        # fantasy_universe = "D&D"
        count += 1
        if count >=5:
            break
        
        # spell = Spell.objects.create(name=name, 
        #     class_type=class_type, 
        #     level=level, 
        #     points=level, 
        #     comical_description=comical_description, 
        #     fantasy_universe=fantasy_universe)
    

    
spell_entry(data)

# Below loops over the API classes and creates them within our db.

# base_url = 'https://www.dnd5eapi.co'

# response = requests.get(base_url + '/api/classes/')

# data = response.json()

# for d in data['results']:
#     new_class = d['name']
#     ClassType.objects.create(name=new_class)







