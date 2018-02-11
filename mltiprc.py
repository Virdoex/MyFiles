#!/usr/bin/env python
import socket
import multiprocessing
import sys
def handle(connection,address):
	import logging
	logging.basicConfig(level=logging.DEBUG)
	logger = logging.getLogger('process %r' % (address,))
	try:
		logger.debug("connected %r at %r", connection,address)
		while(1):
			data=connection.recv(1024)
			if data == " " :
				logger.debug("connection closed remotely")
				break
			logger.debug("Recieved data %r", data)
			connection.sendall(data)
			logger.debug("data sent")
	except:
		logger.debug("problem handling")
	finally:
		connection.close()
		
class Server(object):
	def __init__(self,ip,port):
		import logging
		self.logger = logging.getLogger("server")
		self.ip = ip
		self.port = port
	def start(self):
		self.logger.debug("Listening for the client")
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.socket.bind((self.ip,self.port))
		self.socket.listen(1)
		while(1):
			conn,address=self.socket.accept()
			self.logger.debug("Got Connection")
			process = multiprocessing.Process(target=handle,args=(conn,address))
			process.daemon = 1
			process.start()
			self.logger.debug("Started Process %r ",process)
			
if __name__ == "__main__" :
	import logging
	logging.basicConfig(level=logging.DEBUG)
	server = Server("sys.argv[1]",123)
	try :
		logging.info("Listening for the client")
		server.start()
	except:
		logging.exception("Unexcpected Exception")
	
	logging.info("all done")
