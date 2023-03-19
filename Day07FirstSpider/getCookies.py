#Some web user session is put in Cookies
#Thus getting cookies and send it with Request, equals getting user session
#that is to say: we doesn't need to log in
#Still can spider log in information

#we can check cookies under web by developement tool's memory page
#Here recommand the expansion kit which can check/edit: EditThisCookie

import requests
url = 'https://www.google.com'

cookies = {
    'account' : 'testOwO',
    'passwd' : 'testOwO'
}

print(requests.get(url, cookies=cookies).status_code)
#Output: 200
