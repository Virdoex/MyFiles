#!/usr/bin/env python
import socket
import threading

import sys

def help () :

	print """ Usage is python scanner.py hostname """
def ConnCheck(ip,port):
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.connect((ip,port))
	print "port %d" %port
	server.close()
	return
def main() :
	if len(sys.argv[0]) < 1 :
		print "Invalid arguments"

		print help()
		return	
	
	getip = socket.gethostbyname(str(sys.argv))

	
		
	for port in range(20,150) :
		ConnCheck(getip,port)
	return

if __name__=="__main__" :
	main()
