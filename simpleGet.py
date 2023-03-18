import requests

url = 'https://www.google.com' #先將欲發出GET請求的網址存在url
res = requests.get(url) #對url發出GET請求,並將Response包成回傳物件存在res
print(type(res), res) #Output: <class 'request.models.Response'> <Response [200]>
