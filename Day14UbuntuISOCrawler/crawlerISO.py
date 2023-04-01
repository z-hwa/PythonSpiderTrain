import requests
import re
import json
from bs4 import BeautifulSoup

#record iso which will crawler 
versionList = {'22.04/', '20.04/', '18.04/', '16.04/', '14.04/'}

url = 'http://ftp.ubuntu-tw.org/ubuntu-releases/' #ubuntu iso webpage

resultDisc = {} #record result

for version in versionList:
    r = requests.get(url+version) #the download link is directly add version behind the web link
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html5lib') #analyze

    desktopIso = soup.find('a', string=re.compile('ubuntu-\d{2}\.\d{2}\.?\d{0,2}-desktop-amd64\.iso'))['href'] #using regular expression to represent the file which we want
    serverIso = soup.find('a', string=re.compile('ubuntu-\d{2}\.\d{2}\.?\d{0,2}(-live)?-server-amd64\.iso'))['href'] #find server version

    resultDisc[version] = {
        "desktopIso" : desktopIso,
        "serverIso" : serverIso
    }

with open('iso-image.json', 'w', encoding='utf-8') as f:
    json.dump(resultDisc, f, indent=2, sort_keys=True, ensure_ascii=False)

