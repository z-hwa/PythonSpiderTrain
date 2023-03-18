import requests
import json #Json is not ordinal type in python, but it is constructed inside, thus we import it directly

#use dic to sent POST params
data = {'account':'testOwP', 'password':'testOwO'}
url = 'https://zh.wikipedia.org/'
print(requests.post(url, data=data))

#use json to sent POST params
data = json.dumps(data)
url = 'https://zh.wikipedia.org/'
print(requests.post(url, data=data))
