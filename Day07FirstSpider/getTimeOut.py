#time out
#requests sended until get return if exceed the given time, sent back a exception

import requests
r = requests.get('https://www.google.com', timeout=0.00000001)
#set given time

print(r)
#Output: 101 Network is unreachable
