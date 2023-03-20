#using method same as requests
#but need to claim HTMLSession first

from requests_html import HTMLSession
#宣告Session
session = HTMLSession()

r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')
print(type(r.html))

r = session.post('https://ithelp.ithome.com.tw/users/20134430/ironman/4307', data={})
print(type(r.html))
