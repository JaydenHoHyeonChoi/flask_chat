import requests

url = "https://api.thecatapi.com/v1/images/search"

req = requests.get(url).json
print(type(req))
print(req[0][['url']])