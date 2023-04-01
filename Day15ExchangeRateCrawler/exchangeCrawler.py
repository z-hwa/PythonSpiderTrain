import requests
from bs4 import BeautifulSoup

cointype = input('請輸入你想要爬取的幣種匯率：')

url = f'https://www.google.com/search?q={cointype}'
headers = {
        "user-agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0"
}

r = requests.get(url, headers=headers)


soup = BeautifulSoup(r.text, 'html5lib')
ele = soup.find('span', class_='DFlfde SwHCTb') #which represent class of 1 dollars means how many NTD

if ele:
    print(f'目前一{cointype}為{ele.text}台幣')
else:
    print('目前沒有資料')
