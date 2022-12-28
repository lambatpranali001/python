#!/usr/bin/python3
import sys, socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def fun1():
	for j in range (0,1001):
		try:
			s.connect((sys.argv[1], j))
			print(j, "is open")
		except socket.error as lol:
			pass
fun1()
def fun2():
	print(sys.argv)
	for i in sys.argv:
		print(i)
		for j in range (0,1001):
			try:
				s.connect((i, j))
				print(j, "is open")
			except socket.error as lol:
				pass
			
fun2()


