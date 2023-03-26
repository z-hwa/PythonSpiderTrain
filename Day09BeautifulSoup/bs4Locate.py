#using find(): return first element satisfied condition, return string
#if not return None

#find_all(): return all element satisfied condition, return list
#if not retunr []

#soup.select(): Css selecter

#could using tag, id and class to locate elements
#Ex. soup.find('p', id='myid', class_='myclass')

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

#find all text with 'a'
links = soup.find('a', class_='qa-list__title-link')

print(links['href'].strip())
