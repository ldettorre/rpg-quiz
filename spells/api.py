import requests
import json


base_url = 'https://www.dnd5eapi.co/api/'

def print_json(obj):
    data = json.dumps(obj, sort_keys=True, indent=4)
    print(data)

response = requests.get(base_url + 'spells/time-stop')
print(response.status_code)

print_json(response.json())

