#the first crawler code
#spider the result that google IThome

#But it doesn't do any data cleaning or lock
#Worse-reading(dom, HTML)

import requests
url1 = 'https://www.google.com/search?q=IThome&oq=IThome'
res = requests.get(url1)

print(res.text) #output text in Response
#Output:
#<!doctype html><html lang="zh-TW"><head><meta charset="UTF-8"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" ...
