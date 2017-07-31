import httplib  
conn = httplib.HTTPConnection("192.168.20.201",10080,False,100)  
conn.request('post', '/')  
print conn.getresponse().read()  
conn.close()