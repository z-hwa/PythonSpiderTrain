#search
#syntax: search(template)
#return the first string which satifies the part of '{}' of template 
#template: string mode

from requests_html import HTMLSession

session = HTMLSession() #create session
r = session .get('https://ithelp.ithome.com.tw/users/20134430/ironman/4307') #get https

#print(r.html.text)
ele = r.html.xpath('/html/body/div[2]/div/div/div[2]/div[1]')

#using search to find string in {}
print(ele[0].search('【Day {}】'), ele[0].search('【Day {}】').fixed)
