import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Gossiping/index.html' #url is ptt
cookies = {
        'over18': '1'
} #set cookie over18 to cross the check of is18 on ptt website

resp = requests.get(url, cookies=cookies) #get url
soup = BeautifulSoup(resp.text, 'html5lib') #data clean by bs4
arts = soup.find_all('div', class_='r-ent') #find all data with <div> and class 'r-ent'

#loop find title, link and title
for art in arts:
    title = art.find('div', class_='title').getText().strip()
    link = 'https://www.ptt.cc' + art.find('div', class_='title').a['href'].strip()
    author = art.find('div', class_='author').getText().strip()
    print(f'title: {title}\nlink:{link}\nauthor:{author}')
