#Author SX-ANON16
#github : https://github.com/Noxipom12/
#Facebook : https://www.facebook.com/profile.php?id=100091595902973

import socket
import requests
import pprint
import json

#host name untuk memasukan web
hostname = input('masukan nama domain: ')
#variabel dan untuk melihat ip addres dari web di atas gunakan module socket.gethostbyname
ip_addres = socket.gethostbyname(hostname)

request_url = 'https:geolocation-db.com/jsonp/' + ip_addres
response = request.get(request_url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip("(")
geolocation = json.loads(geolocation)
for k,v in geolocation.items():
    pprint.pprint(str(k) + ' : ' + str(v)