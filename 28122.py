#!/usr/bin/python3
import requests
def fun():
	url ="https://gochanakya.com/registration_ajax/"
	h = {"origin":"https://gochanakya.com","referer":"https://gochanakya.com/registration/","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36","cookie":"_ga_13CF95DJC5=GS1.1.1672208961.1.1.1672209001.0.0.0; _ga=GA1.1.556103035.1672208962; CAKEPHP=bf249016f1d4dff5950ab4b6b6c2b6b9; _fbp=fb.1.1672208978043.618489722"}
	pay = {"first_name":"kjh","phone_verify":"0","last_name":"xyz","user_id":"","work_phone":"7774863033"}
	r = requests.post(url, headers=h, data=pay, timeout=10)
	print(r.status_code)
	print(r.json())
try:
	fun()
except Exception as er:
	print("Problem:", er)


