import socket, select
def runserver()
	"""
	sample multiclients server with use select.

	"""
	port = 8010
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('',port))
	sock.listen(5)
	input = [sock]

	while True:
		r,w,e = select.select(input,[],[])
		for event in r:
			if event == sock:
				client, address = sock.accept()
				client.send("hello")
				print "connect from %s" % str(address)
				client.close()
			else:
				print "pass"


runserver()