# encoding: utf-8

import socket
import random
import select


class game_server(object):
  """
  game Server.
  """
  MAX_CLIENT = 50
  DEBUG = True
  
  def geretate_digit(self, secret=100):
    self.secret = random.randint(1, secret)
    if self.DEBUG: print "game_server:geretate_digit -> self.secret %d" % self.secret
    return self.secret

  def __init__(self, port=8000):
    self.port = port
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.bind(('',self.port))
    self.socket.listen(self.MAX_CLIENT)
    if self.DEBUG: print "game_server:__init__ -> isGood!"
    
  def loop(self):
    count_round = 0
    
    while True:
      count_round += 1
      print "round %d" % count_round
      self.geretate_digit(100)
      if self.DEBUG: print "loop->secret: %d" % self.secret
      is_win = False
      is_dirty = 0
      clients = []
      listen =[self.socket]

      while not is_win:
        print "is_dirty: %d" % is_dirty
        r,w,e = select.select(listen, [], [], 1)
        for i in r:
          if i == self.socket:
            clients.append(client(i))
            print "connect client "
          else:
            pass
        
        if self.DEBUG: print "clients"; print clients
        for user in clients:
          user.accept()
          you_answer = user.recv()
          print "client answer: %d" % (you_answer)
          if self.secret == you_answer:
            #WIN
            is_win = True
            result = "you Win"
            print "win %d" % user
            for cl in users:
              # cl.send("game over.")
              cl.close()
          else:
            result = "Than less" if self.secret > you_answer else "Than bigger"
          
          if self.DEBUG: print "user - result %s" % (result)
          user.sendall(result)
          
          if not is_win: is_dirty += 1



class client(object):
  """docstring for client"""
  DEBUG = True
  def __init__(self, socket, name=1):
    self.name = name
    self.socket = socket
    if self.DEBUG: print "client.__init__ - true"
  
  def accept(self):
    self.socket.accept()

  def send(self, data):
    data = str(data)
    if self.DEBUG: print "client.send(%s)" % data
    self.socket.send(data)

  def recv(self):
    self.data = int(self.socket.recv(1024))
    if self.DEBUG: print "%s = client.recv()" % self.data
    return self.data


server = game_server()
server.loop()