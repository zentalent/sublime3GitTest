import socket
import requests
import Account_pb2 
import Common_pb2
import MessageId_pb2
import pprint


PlayerLogin = Account_pb2.CS_AccountLogin()
PlayerLogin.account = 'newtest123'
PlayerLogin.password = 'd41d8cd98f00b204e9800998ecf8427e'

selectServer = Common_pb2.CS_SelectServer()




headers = {'MessageId': '13'}
cookies = {'':''}
buffersize = 1024
url_login  = r"http://192.168.20.201:8080/GatewayServer/game/ProtoReceiver"
login_params = PlayerLogin.SerializeToString()
print 'login_p:',login_params

def encrypt(src):
	if len(src)>3 :
		dest = []
		print len(src)
		leftLength = len(src) >> 2 
		print leftLength
		rightLength = len(src) - leftLength
		print rightLength
		print dest,len(dest)
		dest[0:rightLength] = list(src[leftLength:rightLength+leftLength])
		print dest,len(dest)
		dest[rightLength:(rightLength+leftLength)] = list(src[0:leftLength])
		print dest,len(dest)
		return dest
	else:
		return src

s = requests.Session()
datasend = encrypt(login_params)
print datasend,type(datasend)

def toByteArray(src):
	data1 = bytearray()
	for i in src:
		i = ord(i)
		data1.append(i)
	return data1

def decrypt(src):
	if len(src)>3:
		dest = []
		rightLength = len(src)>>2
		leftLength = len(src) - rightLength
		dest[0:rightLength] = src[leftLength:leftLength+rightLength]
		dest[rightLength:(leftLength+rightLength)] = src[0:leftLength]
		return dest
	else:
		return src

request = s.post(url_login,toByteArray(datasend),headers = headers)
print request.text
