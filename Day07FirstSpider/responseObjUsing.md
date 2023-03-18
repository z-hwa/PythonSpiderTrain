# 不管使用Request中GET或POST,都會回傳一個回應物件
requests.models.Response

-res.status_code: 該HTTP狀態碼
-res.raw: 原始回應物件urllib3.response.HTTPResponse
		  res.raw.read()讀取
-res.content: 回應物件的位元組序列(bytes)型態
-res.text: 回應物件的字串(str)型態
-res.headers: 回應物件的headers
-res.json():回應物件的JSON格式,會將回應的字串用JSON encode,不必引入JSON
-res.raise_for_ststus():若請求失敗(status code != 200),則拋出錯誤
-res.url: 請求的url
-res.cookies: 請求後的cookies
-res.encoding: 編碼格式

# 更多參數
Requests庫包含
-Requests Headers
-Proxy IP使用
-憑證驗證
-Timeout
-Cookies傳入
...
