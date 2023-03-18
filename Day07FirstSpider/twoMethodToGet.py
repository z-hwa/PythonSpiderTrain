#GET will bring parameter sometimes, which put behind url with '?'.
#If there are many parameters, using '&' to seperate.

#For example
#url: https://www.google.com/search?q=IThome&oq=IThome
#parameter q has value: IThome
#oq has value: IThome

import requests

#方法一
url1 = 'https://www.google.com/search?q=IThome&oq=IThome' #直接將參數放到url
res = requests.get(url1) #Request function
print(f'method 1:\n{res.url}\n{res}\n') 
#Output: https://www.google.com/search?q=IThome&oq=IThome
#<Response [200]>

#方法二
url2 = 'https://www.google.com/search' #Set url
params = {'q':'IThome', 'oq':'IThome'} #Set parameters
res = requests.get(url2, params=params) #Put parameters when using GET
print(f'method 2:\n{res}')
