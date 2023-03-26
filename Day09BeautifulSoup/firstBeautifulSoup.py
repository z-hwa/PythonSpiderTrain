import requests
from bs4 import BeautifulSoup

url = 'https://ithelp.ithome.com.tw/users/20134430/ironman/4307'
#use header to set user agent
headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0'
        }

#sent get requests to url, and put response object in resp
resp = requests.get(url, headers=headers)

#let resp.text (HTML data) define to BeautifulSoup object, using html5lib to analyze HTML content
soup = BeautifulSoup(resp.text, 'html5lib')

#output title of the website
print(soup.title.getText())

#output the first text with <li> element which finded
print(soup.li.getText())

#same as upper one
print(soup.find('li').getText())
