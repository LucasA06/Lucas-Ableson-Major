import requests

api_key = 'e4813eefc4msh22f23665b1c6eabp14e427jsna2d1b1e61863'
url = 'https://api.football-data.org/v2/competitions/2021/standings'

headers = {
    'X-Auth-Token': api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
else:
    print(f'Error: {response.status_code}')