import socket
import urllib2
import urllib
import Account_pb2 
import Common_pb2
import MessageId_pb2
from ctypes import *

PlayerLogin = Account_pb2.CS_AccountLogin()
PlayerLogin.account = 'newtest123'
PlayerLogin.password = 'd41d8cd98f00b204e9800998ecf8427e'


getServerList = Account_pb2.SC_AccountLogin()
getServerId = Common_pb2.VO_ServerInfo()

print type(getServerList.serverInfos)


selectServer = Common_pb2.CS_SelectServer()


headers = {'MessageId': 13}
cookies = {''}

url_login  = r"http://192.168.20.201:8080/GatewayServer/game/ProtoReceiver"


login_params = PlayerLogin.SerializeToString()


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


datasend = encrypt(login_params)

def toByteArray(src):
	data1 = bytearray()
	for i in datasend:
		i = ord(i)
		data1.append(i)
	return data1

request = urllib2.Request(url_login,toByteArray(datasend),headers = headers)

response = urllib2.urlopen(request)
print decrypt(response.readlines())
