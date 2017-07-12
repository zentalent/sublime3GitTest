# -*- coding: utf-8 -*-
# -*- coding: gbk -*-

import sys
from sys import argv
import svn.local
import os
reload(sys)
sys.setdefaultencoding("utf8")





#UnityPath,bundleIdentifier,serverpath,updateSVN,debugVersion,bundleVersion = argv
UnityPath = 'C:\Program Files\Unity\Editor\Unity.exe'
bundleIdentifier = 'E:\DLLFiles\Version'
serverpath = 'com.tencent.tmgp.fxzjxx'
updateSVN = 'ceshifu$http://192.168.20.201:8080/GatewayServer/game/ProtoReceiver'
debugVersion = 'false'
bundleVersion = '1.3.44076'
channelId = '1'
PROJECT_PRJPATH = 'E:\TankWar1'
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


print os.system("del /f/s/q %s\Assets\Plugins\Android\*.aar" % PROJECT_PRJPATH)
print os.system("copy /y %s\\Data\\Channel\\%s\\*.* %s\\Assets\\Plugins\\Android" % (PROJECT_PRJPATH,channelId,PROJECT_PRJPATH))

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


os.system('java -jar "%s\\apktool.jar" d -f -s %s\%s -o %s\\tmp' \
			% (apktool,APK_PATH,apkName,APK_PATH))
print "APK unpacked Succeed"

os.system("copy /y %s\\MonoEncrypt\\release\\armeabi-v7a\\libmono.so %s\\tmp\lib\\armeabi-v7a\\" % (DLLFiles,APK_PATH))
print "SUCCESS COPY libmono.so"

def unpack():
	os.system('java -jar "%s\\apktool.jar" b "E:\\DLLFiles\\Version\\tmp" -o %s\\tmp1.apk'\
			 % (apktool,APK_PATH))

unpack()



	
		