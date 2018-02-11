#!/usr/bin/env python
import socket
from threading import Thread
from SocketServer import ThreadingMixIn

class ClientThread(Thread):
	def __init__(self,ip,port):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		print "New multithread server started for" + ip + ":" + str(port)
	def run(self):
		data = conn.recv(1024)
		print "client send",data
		Message = raw_input("Multithread Python Server:ENter response")
		conn.send(Message)

tcpsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpsocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

tcpsocket.bind(("0.0.0.0",9003))
threads = []
while(1):
	tcpsocket.listen(4)
	print "[+]Listenting for the client:"
	(conn,(ip,port)) = tcpsocket.accept()
	newThread = ClientThread(ip,port)
	newThread.start()
	threads.append(newThread)


for t in threads:
	t.join()	
