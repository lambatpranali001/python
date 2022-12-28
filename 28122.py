#!/usr/bin/python3
import sys
def fun():
	domain = sys.argv[1]
#	print(domain)
	i = sys.stdin.readlines()
#	print(i)
	k = i[::-1]
#	print(k)
	for item in i:
#		print(item)
		p1 = print("http://"+item.strip("\n")+"."+domain)
		p2 = print("http://"+item.strip("\n")+"0."+domain)
		for kitem in i:
			if item.strip() != kitem.strip():
				p3 = print("http://"+item.strip("\n")+"."+kitem.strip("\n")+"."+domain)
				p4 = print("http://"+item.strip("\n")+"0."+kitem.strip("\n")+"."+domain)
				p5 = print("http://"+item.strip("\n")+"."+kitem.strip("\n")+"0."+domain)

fun()

def save():
	for i in range(0,5):
		urls = print(p) 
