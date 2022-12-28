#!/usr/bin/python3
import requests, sys
try:
	for u in sys.stdin.readlines():
		url = u.strip("\n")
		print(type(u))
		h = {'User-Agent':'Mozilla'}
		r= requests.get(url, headers=h, timeout = 10)
		print("the response is: ", r.status_code)
except Exception as call:
	print("Problem:", call)
