#!/usr/bin/python3
import socket
s = socket.socket()
host = "192.168.50.145"
port = 8888
try:
	s.connect((host, port))
	print(port, "is open" )
except socket.error as lol:
	print(port, "is close")

