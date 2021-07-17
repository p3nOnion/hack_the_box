import pwn
import requests
import base64
import hashlib
url = 'http://206.189.17.217:31995/'

req= requests.Session()
rget= req.get(url=url)

text= rget.text.split('\'center\'>')[2].split('</h3>')[0]

print(text.encode('utf-8'))

md5_text= hashlib.md5(text.encode('utf-8')).hexdigest()
print(md5_text)
rpost = req.post(url=url, data= dict(hash=md5_text))
print(rpost.text)