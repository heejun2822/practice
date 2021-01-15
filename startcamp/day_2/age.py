import requests

name = 'harry'
url = f'https://api.agify.io/?name={name}'

response = requests.get(url).json()
print(response)