from socket import *
"""
	sample client:
		connect to server:port (tcp)
		recv data 
		print data
		
"""
server = 'localhost'
port =8000

client = socket(AF_INET, SOCK_STREAM)
client.connect((server,port))
ctm = client.recv(1024)
client.close()
print "now %s" % ctm.decode('ascii')