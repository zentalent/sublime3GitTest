# -*- coding: utf-8 -*-
# -*- coding: gbk -*-

import sys
from sys import argv
import svn.local
import os
reload(sys)
sys.setdefaultencoding("utf8")

channelId = '1'
PROJECT_PRJPATH = 'E:\TankWar1'



UnityPath,bundleIdentifier,serverpath,updateSVN,debugVersion,bundleVersion = argv
packName = '44306'
channel = '3$11'
sub_channel = '301$MAIN'
DLLFiles ="E:\DLLFiles"
APK_PATH = DLLFiles+"\\Version"
LogPath = DLLFiles+"\\LogFile\\buildAPK_Main.txt"
svnVersion = '44380'
apktool = 'E:\\DLLFiles\\apktool'
finalapkpath = u'\\\\Server1\\开发存档（正式）\\Version\\正式包\\android\\'.decode('utf8').encode('gbk')
DLL_PATH= APK_PATH+"\\tmp\\assets\\bin\\Data\\Managed\\Assembly-CSharp.dll"
buildDLL = 'false'
jarsigner = "C:\\Program Files\Java\\jdk1.7.0_80\\bin\jarsigner.exe"

def findapkname(apkpath):
	for file in os.listdir(apkpath):
		if os.path.splitext(file)[1] =='.apk':
			return file
		

apkName = findapkname(APK_PATH)
print APK_PATH
print apkName
print 'Gained apk file name'

#@rem unpack apk 
#@call %apktool%\apktool.bat d -f -s %APK_PATH%\!apkName! -o %APK_PATH%\tmp
                                 
#@del /f/s/q %APK_PATH%\!apkName!
#os.putenv(apktool)
def unpack():
	os.system("java -jar %s\\apktool.jar %s %s %s %s %s %s %s %s %s d -f -s %s\%s -o %s\\tmp" \
	% (apktool,PROJECT_PRJPATH,bundleIdentifier,serverpath,debugVersion,updateSVN,bundleVersion,packName,channel,sub_channel,APK_PATH,apkName,APK_PATH))

print "------start unpacking-------"

if unpack() == 1:
	print 'apk unpack failed'
else:
	print "APK unpacked Succeed"
	os.system("%s\\MD5Project\\MD5Project.exe DLL %s" % (DLLFiles,DLL_PATH))
	print"SUCCESS encrypt DLL"
	if buildDLL== 'true' :
		#@rem copy DLL
		
		os.system("copy /y %s \"%s\" " % (DLL_PATH,finalapkpath))
		print "SUCCESS COPY DLL"

	os.system("copy /y %s\\MonoEncrypt\\release\\armeabi-v7a\\libmono.so %s\\tmp\lib\\armeabi-v7a\\" % (DLLFiles,APK_PATH))
	print "SUCCESS COPY libmono.so"
	
	#rem 压缩
	os.system("%s\\apktool.bat b %s\\tmp -o %s\\tmp1.apk" % (apktool,APK_PATH,APK_PATH))
	print "SUCCESS 压缩"

	#rem resign
	os.system("%s -storepass fanxing2016 -keystore %s\keystore.keystore -signedjar %s\%s %s\\tmp1.apk fxzjxx" % (jarsigner,apktool,APK_PATH,apkName,APK_PATH))
	os.system("del /f/s/q %s\\tmp1.apk" % (APK_PATH))
	print "Resign Succeed"
	
	if buildChannel=='true' :
		#rem push original chennal pack
		os.system("copy  /y %s\%s %s\Channel\\" % (APK_PATH,apkName,APK_PATH))
		#@echo !apkName!>%APK_PATH%\Channel\tmp.txt
		print "SUCCESS to push original channel pack"
	

	os.system("rd /s/q %s\\tmp" % APK_PATH)
print 'Copy apk to \\server1'
os.system("copy /y %s\\*.apk %s" % (APK_PATH,finalapkpath))
os.system("del /f/q %s\\*.apk" % APK_PATH)
print 'copying succeed'
		


	
		