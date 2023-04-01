import requests
import json
from bs4 import BeautifulSoup

articleList = [] #save article which used to save in JSON

def GetResp(url):
    cookies = {
            'over18': '1'
    } #set cookie over18 to cross the check of is18 on ptt website
    
    resp = requests.get(url, cookies=cookies) #get url
    
    if resp.status_code != 200:
        return 'error'
    else:
        return resp

def GetArticles(resp):
    soup = BeautifulSoup(resp.text, 'html5lib') #data clean by bs4
    arts = soup.find_all('div', class_='r-ent') #find all data with <div> and class 'r-ent'

    #loop find title, link and title
    for art in arts:
        title = art.find('div', class_='title').getText().strip()
        #prevent from the error of not finding link
        if not title.startswith('(本文已被刪除)'):
            link = 'https://www.ptt.cc' + art.find('div', class_='title').a['href'].strip()
        author = art.find('div', class_='author').getText().strip()
        #print(f'title: {title}\nlink:{link}\nauthor:{author}')
        
        #dictionary used to save article data
        article = {
                'title' : title,
                'link' : link,
                'author' : author
        }
        articleList.append(article)

    nextUrl = 'https://www.ptt.cc' + soup.select_one('a.wide:nth-child(2)')['href']
    return nextUrl

#satisfy when running this program
if __name__ == '__main__':
    #first url
    url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

    #let crawler climb 10 pages
    for nowPageNumber in range(10):
        resp = GetResp(url)

        #check url is get successful
        if resp != 'error':
            url = GetArticles(resp)
        print(f'=========={nowPageNumber+1}/10============')

    #open file and save as Json file
    with open('ptt-articles.json', 'w', encoding='utf-8') as f:
        json.dump(articleList, f, indent=2, sort_keys=True, ensure_ascii=False)
