import socket 
from socket import *

Host = '192.168.20.201'
Port = 10080
BUFSIZ = 1024
ADDR = (Host,Port)
username = 'fanxing2016'
password = 'fanxing2016'

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
print "connected"
tcpCliSock.send('1004')
print "send data..."
tcpCliSock.recv(1024)
print "recv data..."
tcpCliSock.close()  