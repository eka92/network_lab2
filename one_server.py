from socket import *

port=5001

print "set port %d" % port
server = socket(AF_INET, SOCK_STREAM)
server.bind(('',port))
server.listen(5)
while True:
	client, addres = server.accept()
	print "connect from %s" % str(addres)
	client.send("hello!")
	client.close()
	