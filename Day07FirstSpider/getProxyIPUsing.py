#using proxy IP which is called prxy server(代理伺服器)

#what does proxy IP do?
#1. faster accesss speed
#2. hide your IP
#3. firewall(防火牆)
#4. relieve region limit

#difference between Proxy and VPN
#Proxy cannot block AD and encrypt data
#Proxy using on specific web
#Proxy's firewall is using to protext inside network

#we can use free Proxy list
#Ex. https://geonode.com/free-proxy-list

import requests
url = 'https://snake-game-backend.herokuapp.com/Alldatas'
proxies = {'http' : 'http://50.235.149.74:8080', 'https' : 'https://74.143.86.243:3128'} #set proxy IP

print(requests.get(url, proxies=proxies).status_code)
#Nothing?
