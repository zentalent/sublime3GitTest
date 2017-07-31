import Account_pb2 
import socket
import httplib


HOST = '192.168.20.201'    # The remote host
PORT = 8080              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
PlayerLogin = Account_pb2.CS_AccountLogin()
PlayerLogin.account = 'newtest123'
PlayerLogin.password = '111'

SendDataStr = PlayerLogin.SerializeToString()

Serverlist = Account_pb2.SC_AccountLogin()

s.send(SendDataStr)
print SendDataStr
print s.recv(10000)
