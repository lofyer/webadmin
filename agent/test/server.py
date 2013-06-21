import socket

address = ('127.0.0.1',8765)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)

ss, addr = s.accept()
print "Connected with ", addr

ss.send('Bye')
rc = ss.recv(1024)
print rc

ss.close()
s.close()
