#!/usr/bin/env python

import socket

from threading import Thread
import os
import sys

server = raw_input("Please enter the server name")
global num
def portconnect() :
	try :
		serv_ip = socket.gethostbyname(server)
		print "Please Wait scannin remote host",serv_ip
		for port in range(num):
			sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			conn = sock.connect((serv_ip,port))
			if conn == 0 :
				print "port {}: open :",format(port)
			sock.close()
	except socket.gaierror :
		print """
				I Can't find the server
                       """
		sys.exit()
for i in range(1):
	t = Thread(target=portconnect,args=(num=100))
	t.start()
