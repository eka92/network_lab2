# coding: utf-8
from socket import *
"""
  Самый простой способ организации однопользовательской игры

"""
secret = 42
my_socket = socket(AF_INET, SOCK_STREAM)
my_socket.bind(('',8000))

try:
  my_socket.listen(5)
except Exception, e:
  print e
  exit()

not_game = False
client, addr = my_socket.accept()
print "connect from %s" % str(addr)
while not not_game:
  data = client.recv(1023) #name
  print "Client name is %s" % data
  client.send("OK")

  end_round =  False
  while not end_round:
    data = client.recv(1024)
    print "RAW DATA ", data
    data = int(data)
    print "INT DATA ", data
    if  data > secret:
      report = ">"
    elif data < secret:
      report = "<"
    else:
      report = "="
      end_round = True

    client.send(report)


  print "end round"
  not_game =  True
  client.close()
my_socket.close()
