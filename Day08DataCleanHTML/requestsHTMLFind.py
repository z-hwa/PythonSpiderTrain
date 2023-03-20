#語法:find(selector, containing, clean, first, _encoding)
#selector: CSS語法選擇器
#containing: 傳入字串,使定位到的元素包含該字串,預設為None
#clean: 是否清除並忽略HTML中標籤, 預設為False
#first: 是否只尋找到第一個定位到的元素,預設為False
#_encoding: 編碼格式,預設為None

from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')

#using CSS syntax choosing to find
ele = r.html.find('body > div.container.index-top > div > div > div.board.leftside.profile-main > div.ir-profile-content')

print(ele[0].text)
