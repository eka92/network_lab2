import socket

class client():
  def __init__(self, port=8000, addres='localhost'):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.addres = addres
    self.port = port
    self.socket.connect((addres,port))

  def check(self, digit):
    self.socket.send(digit)
    result = self.socket.recv(1024)
    print result

  def delete(self):
    self.socket.close()
    
me = client()
me.check("90")