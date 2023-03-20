#following are roughly data claening method

from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')

print(r.html.url) #output url of the website

print(r.html.links) #output all url inside website

print(r.text) #output content of the website(include HTML)

print(r.html.text) #output content of the website(remove HTML)

