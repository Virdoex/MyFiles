#!/usr/bin/env python
import socket
import subprocess
import os
from datetime import datetime
import sys
subprocess.call('clear',shell=1)
remoteServer = raw_input("Enter the server name:")
remoteIp = socket.gethostbyname(remoteServer)

print "_"*60
print "Wait scanning remote host:",remoteIp
print "_"*60
t1 =datetime.now()

try :
	for port in range(1,1025):
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result = sock.connect_ex((remoteIp,port))
		if result == 0:
			print "Port {}:Open".format(port)
		sock.close()

except socket.gaierror:
	print "Hostname could not be resolved"
	sys.exit()
t2 = datetime.now()
total = t2-t1
print "Scanning completed in",total
