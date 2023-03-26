#Search_all
#syntax: search_all(template)
#like function 'search'

from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307')

# print(r.html.text)
ele = r.html.xpath('/html/body/div[2]/div/div/div[2]/div[1]')

#print all
print(ele[0].search_all('【Day {}】'))

#print one by one
for day in ele[0].search_all('【Day {}】'):
    print(day.fixed)
