# coding: utf-8
from socket import *
im random
"""
  Самый простой способ организации одноклиенской игры

"""

client_socket = socket(AF_INET, SOCK_STREAM)
try:
  client_socket.connect(('localhost',8000))
except Exception, e:
  print e
  exit()
client_socket.send("Clien1")
print "connected"
data = client_socket.recv(1023)
if data == "OK":
  print "OK"
# data = raw_input("value: ")
# data = str(int(data))
# data = str(42)
result = ">"

while result != "=":
    # data = str(random.randint(0,50))
    data = raw_input("you VARIANT: ")
    data = str(int(data))
    print "VARIANT:", data
    client_socket.send(data)
    result = client_socket.recv(1023)
    print result

client_socket.close()