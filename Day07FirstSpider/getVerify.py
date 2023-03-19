#The website's https not secure since certificate fail
#Request cannot spider since no secure
#But requests cuold close the certificate which let Requests success to spider

import requests
r = requests.get('https://www.google.com', verify = False) #close certificate

print(r.status_code) #Output: 200

#Warning when using print(r.status_code())
#:int object is not callable

#Thus changed to r.status_code
