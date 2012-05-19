# encoding: utf-8

import socket
import random
import select

class game_server(object):
  """
  game Server.
  """
  MAX_CLIENT = 50
  
  def geretate_digit(self, secret=100):
    self.secret = random.randint(1, secret)
    return self.secret

  def __init__(self, port=8000):
    self.port = port
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.bind(('',self.port))
    self.socket.listen(self.MAX_CLIENT)
    
  def loop(self):
    count_round = 0
    while True:
      count_round += 1
      print "round %d" % count_round
      self.geretate_digit(100)
      is_win = False
      is_dirty = 0
      clients = []
      listen =[self.socket]
      while not is_win:
        r,w,e = select.select(listen, [], [], 1)
        for i in r:
          if i == self.socket:
            clients.append(client(r))
          else:
            pass
        for user in clients:
          you_answer = clients[user].recv()
          if self.secret == you_answer:
            #WIN
            is_win = True
            result = "you Win"
            print "win %d" % user
          else:
            result = "Than less" if self.secret > you_answer else "Than bigger"
          client.sendall(result)
          if not is_win: is_dirty += 1


class client(object):
  """docstring for client"""
  def __init__(self, socket):
    self.socket = socket
  
  def send(self, data):
    self.socket.sendall(data)

  def recv(self):
    self.data = self.socket.recv(1024)
    return self.data


server = game_server()
server.loop()