from socket import *
import GM_pb2

Host = '192.168.20.201'
Port = 10080
Bufsize = 1024
ADDR = (Host,Port)

conn = socket(AF_INET,SOCK_STREAM)
conn.connect(ADDR)

while  True:
	username = 'fanxing2016'
	password = 'fanxing2016'
	data = username+password
	conn.send(data)
	conn.recv(100)
	