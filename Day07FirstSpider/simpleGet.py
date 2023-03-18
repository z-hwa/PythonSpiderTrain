import requests

url = 'https://www.google.com' #先將欲發出GET請求的網址存在url
res = requests.get(url) #對url發出GET請求,並將Response包成回傳物件存在res
print(type(res), res) #Output: <class 'request.models.Response'> <Response [200]>

#status code
#200: OK
#301: Moved Permanently
#302: Moved Temporarily
#400: Bad request(用戶端錯誤)
#401: Unauthorized(未授權,請求攜帶憑證)
#403: Forbidden(沒有權限)
#404: Not Found
#418: I'm a teapot(愚人節彩蛋)
#500: Internal Server Error(伺服器端錯誤)
#502: Bad GateWay(一般來說是伺服器的某個服務沒有正確執行)
#503: Service Unavailable(伺服器臨時維護或是快掛了,暫時無法處理請求,臨時流量過大)
#504: Gateway Timeout(伺服器上的服務沒有回應)
