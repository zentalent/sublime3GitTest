import os
import sys

ProtoPath = r'E:\proto\proto_src'
os.chdir(ProtoPath)
for i in os.listdir(ProtoPath):
	print os.getcwd()
	print i
	cmd = 'protoc --python_out=./ '+i
	print cmd
	os.system(cmd)

