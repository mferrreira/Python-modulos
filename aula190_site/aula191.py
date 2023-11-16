# requests para requisições
# Tutorial -> youtu.be/Qd8JT0bnJGs

import requests

# http:// -> 80
# https:// -> 443

url = 'http://0.0.0.0:8000'

response = requests.get(url)

print(response)
#print(response.text)
#print(response.content)
#print(response.status_code)
#print(response.json)
#print(response.text)