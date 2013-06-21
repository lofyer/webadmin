import socket

address = ('127.0.0.1', 8765)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

data = s.recv(1024)
print "Received data is %s" % data

s.send('I\'m message from clinet')

s.close()
