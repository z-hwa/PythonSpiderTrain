#xpath
#syntax: xpath(selector, clean, first, _encoding)

#selector: xpath chooser
#clean: Is it clean and ignore tag of HTML, default is False
#first: Is it find until the first element, default is False
#_encoding: encoding type, default is False

from requests_html import HTMLSession

session = HTMLSession() #create session
r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307') #get by https

ele = r.html.xpath('/html/body/div[2]/div/div/div[2]/div[1]') #use xpath to cleaning data

print(ele[0].text)
