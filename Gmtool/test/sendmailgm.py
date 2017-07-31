from socket import *
import MessageId_pb2
import Message_pb2
import struct

Host = '192.168.20.201'
Port = 10080
ADDR = (Host,Port)

sendmail = Message_pb2.CS_SendEmail()
sendmail2 = Message_pb2.CS_SendEmail()
msg = MessageId_pb2.MICS_SendEmail
msgIdArray = list(str(msg))

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


def toByteArray(src):
	data = bytearray()
	for i in src:
		i = ord(i)
		data.append(i)
	return data
	print src.title,data

prop = sendmail.itemList.add()
prop.id = 201
prop.type = 201
prop.count = 1

sendmail.serverId = 1007
sendmail.userId = 101036
sendmail.title =''
sendmail.desc = ''

maildata = encrypt(sendmail.SerializeToString())
#messagelength + id +content
sendata = bytearray()
datalength = list(str(len(maildata)+7))
print datalength
sendata.append(toByteArray(datalength))
print sendata[0]
sendata.append(toByteArray(msgIdArray))
sendata.append(maildata)


gmclient = socket(AF_INET,SOCK_STREAM)
gmclient.connect(ADDR)
print 'Gm Server is connected'
#gmclient.send(bytes(sendata))
print 'datasend'
#buff = gmclient.recv(1024*4)
print len(buff)
gmclient.close()
print 'Disconnected '