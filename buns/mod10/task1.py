import requests
import json

data = json.loads(requests.get('https://swapi.dev/api/starships/10/').text)
listOfPilots = []
for item in data['pilots']:
  info = json.loads(requests.get(item).text)
  pilot = {'name': info['name'],
          'height': info['height'],
          'mass': info['mass'],
          'homeworld': json.loads(requests.get(info['homeworld']).text)['name'],
          'homeworld_url': info['homeworld']}
  listOfPilots.append(pilot)

ship = {'name': data['name'],
        'max_atmosphering_speed': data['max_atmosphering_speed'],
        'starship_class': data['starship_class'],
        'pilots': listOfPilots}

with open('data.json', 'w') as file:
  json.dump(ship, file, indent=4)
print(json.dumps(ship, indent=4))
