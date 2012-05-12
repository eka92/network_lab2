import socket
import threading
"""
	for testing server
"""
count_thread = 50
server = 'localhost'
port = 8010

class client(threading.Thread):
	def __init__(self, name_thread=None, type_socket=1):
		self.name_thread = name_thread
		type_socket = socket.SOCK_STREAM if type_socket == 1 else socket.SOCK_DGRAM
		self.sock = socket.socket(socket.AF_INET, type_socket)
		print "create socket"

	def run(self, to_connect):
		self.sock.connect(to_connect)
		print "connect to %s:%d" % (to_connect[0], to_connect[1])
		data = self.sock.recv(1024)
		print self.name_thread
		print data


for i in xrange(count_thread):
	print "%d thread create" % i
	client(i,1).run((server,port))