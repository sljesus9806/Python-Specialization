import requests


url_auth = 'http://flex.archfx.io/api/v1/auth/api-jwt-auth/'
payload = {
    'username': 'jsalazar@archsys.io',
    'password': 'Pergolesi1@'
}
response = requests.post(url_auth, json=payload)

#extracting the token

token = response.json()
print('Token:', token)

#using the token to get the data

hearders = {
    'Authorization':f'JWT {token}',
    'content-type':'application/json'
}

url_machine = 'http://flex.archfx.io/api/v1/machine/d--0000-0001-0000-1234'
response = requests.get(url_machine, headers=hearders)

#Print data

print('Machine data:', response.json())