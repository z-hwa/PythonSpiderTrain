#Since some page will block
#using header to avoid access deny

import requests
url = 'https://snake-game-backend.herokuapp.com/alldatas' #set url
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36' #set user_agent

#set header with user_agent
headers = {
    'User_Agent' : User_Agent
}

print(requests.get(url, headers=headers).status_code)
#Output: 404
