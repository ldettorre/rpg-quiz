import requests
import json
from .models import ClassType, Spell


base_url = 'https://www.dnd5eapi.co'

''' Class API Resource '''
# response = requests.get(base_url + '/api/classes/')

''' Spells API Resource '''
# response = requests.get(base_url + '/api/spells/')

''' Features API Resource '''
response = requests.get(base_url + '/api/features/')

data = response.json()

def class_entry(obj):
    '''Below loops over the API classes and creates them within our db.'''
    for d in data['results']:
        new_class = d['name']
        ClassType.objects.create(name=new_class)


def spell_entry(obj):
    ''' Loop over each spell for it's url, then use the url in a request to access
    all the other data in that individual spell. Once the data has been 
    to a variable, we create a new spell object and add classes '''

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
    
        spell = Spell.objects.create(
            name=spell_name, 
            level=spell_level, 
            points=spell_level, 
            comical_description=spell_desc, 
            fantasy_universe=spell_universe)
        for i in new_classes:
            spell.class_type.add(i)
    


def feature_entry(obj):
    ''' Loop over every feature within the feature resource for its url. Then
    use the url to pull the neccesary data and create a new object. Features
    with no levels are set as 0 by default thanks to the try/except for KeyErrors'''

    features = obj
    for i in data['results']:
        feature = requests.get(base_url + i['url'])
        feature_name = feature.json()['name']
        feature_class = feature.json()['class']['name']
        new_classes = []

        existing_classes = ClassType.objects.all()
        for e in existing_classes:
            if feature_class == e.name:
                new_classes.append(e.id)
        try:
            feature_level = feature.json()['level']
        except KeyError:
            print("This feature has no level. Default will be set to 0")
            feature_level = 0
        feature_desc = feature.json()['desc']  
        feature_universe = "D&D"
        feature_ability = "Feature"

        spell = Spell.objects.create(
            name=feature_name,
            level=feature_level, 
            points=feature_level, 
            comical_description=feature_desc,
            ability_type=feature_ability,
            fantasy_universe=feature_universe)
        for i in new_classes:
            spell.class_type.add(i)


feature_entry(data)