#parameters are put in message body, not url
#In POST, we could use many difference type methods to bring parameters
#Ex, dictionary, tuple, list, JSON
#Here recommand JSON and dictionary

import requests
import json #Json is not ordinal type in python, but it is constructed inside, thus we import it directly

#use dic to sent POST params
data = {'account':'testOwP', 'password':'testOwO'} #set parameters
url = 'https://zh.wikipedia.org/' #set url
print(requests.post(url, data=data)) #Output; <Response 405]>

#use json to sent POST params
data = json.dumps(data) #change obj of Python into JSON obj
url = 'https://zh.wikipedia.org/' #set url
print(requests.post(url, data=data)) #Output: <Response [405]>

#error code 405 not allow you to perform a specific action
