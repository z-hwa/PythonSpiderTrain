import requests

#方法一
url1 = 'https://www.google.com/search?q=IThome&oq=IThome' #直接將參數放到url
res = requests.get(url1)
print(res.url, res)

#方法二
url2 = 'https://www.google.com/search' #直接將參數放到url
params = {'q':'IThome', 'oq':'IThome'}
requests.get(url2, params=params)
