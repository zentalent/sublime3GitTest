import socket

tcpserver = socket.socket()

Host = '192.168.0.101'
Port = 12346

tcpserver.bind((Host,Port))

tcpserver.listen(1)

while True :
	c ,addr = tcpserver.accept()
	data = c.recv(1024)
	print 'connection address' , addr,data
	c.sendall('data')
	c.close()