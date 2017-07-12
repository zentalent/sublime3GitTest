# -*- coding: utf-8 -*-
# -*- coding: gbk -*-
#coding = gbk
import sys
from sys import argv
import svn.local
import os
reload(sys)
sys.setdefaultencoding('utf-8')
#bundleIdentifier,serverpath,debugVersion,updateSVN,bundleVersion,packName,channel,sub_channel,buildChannel,buildDLL = argv
bundleIdentifier = os.getenv("bundleIdentifier")
serverpath = os.getenv("serverpath")
updateSVN = os.getenv("updateSVN")
debugVersion = os.getenv("debugVersion")
bundleVersion = os.getenv("bundleVersion")
packName = os.getenv("packName")
channel = os.getenv("channel")
print type(channel)
sub_channel = os.getenv("sub_channel")
buildChannel = os.getenv("buildChannel")
buildDLL = os.getenv("buildDLL")
print type(buildDLL)

UnityPath = "C:\\Program Files\\Unity\\Editor\\Unity.exe"
PROJECT_PRJPATH = "D:\\TankPrj1\\Prj\\TankWar1_Taptap"
DLLFiles ="D:\\TankPrj1\\Prj\\DLLFiles"
APK_PATH = DLLFiles+"\\Version"
LogPath = DLLFiles+"\\LogFile\\buildAPK_Main.txt"
jarsigner = "C:\\Program Files\Java\\jdk1.7.0_80\\bin\jarsigner.exe"
apktool = DLLFiles+'\\apktool'
DLL_PATH= APK_PATH+"\\tmp\\assets\\bin\\Data\\Managed\\Assembly-CSharp.dll"
finalapkpath = "\\\\Server1\\开发存档（正式）\\Version\\正式包\\android\\".decode('utf-8').encode('gbk')

if updateSVN=='true' :
    os.system('cd /d %s' % PROJECT_PRJPATH)
    os.system('svn up')


r = svn.local.LocalClient(PROJECT_PRJPATH)
svnVersion = r.info()['commit#revision']
print svnVersion 

channelId = channel.split('$')[0]
print channelId
os.system("del /f/s/q %s\Assets\Plugins\Android\*.aar" % PROJECT_PRJPATH)
os.system("copy /y %s\\Data\\Channel\\%s\\*.* %s\\Assets\\Plugins\\Android" % (PROJECT_PRJPATH,channelId,PROJECT_PRJPATH))
print 'start packing'
os.system('%s -logfile %s -quit -batchmode -projectPath %s -executeMethod BuildCommand.BuildAndroid \
	start %s %s %s %s %s %s %s %s %s end' \
	% (UnityPath,LogPath,PROJECT_PRJPATH,APK_PATH,bundleIdentifier,serverpath,debugVersion,bundleVersion,packName,svnVersion,channel,sub_channel))

if debugVersion=='false':
	
	#@set apkName=
	#for /f "delims=," %%i in (%APK_PATH%\tmp.txt) do set apkName=%%i
	#os.system('del /f/s/q %APK_PATH%\tmp.txt
	#print 'Gained apk file name'

	def findapkname(apkpath):
		for file in os.listdir(apkpath):
			if os.path.isfile(file) == 'false':
				return os.path.splitext(file)[0]

	apkName = findapkname(APK_PATH)
	print 'Gained apk file name'
	
	#@rem unpack apk 
	#@call %apktool%\apktool.bat d -f -s %APK_PATH%\!apkName! -o %APK_PATH%\tmp
	                                 
	#@del /f/s/q %APK_PATH%\!apkName!
	#os.putenv(apktool)
	os.system("java -jar %s\\apktool.jar %s %s %s %s %s %s %s %s %s d -f -s %s\%s -o %s\\tmp" \
		% (apktool,PROJECT_PRJPATH,bundleIdentifier,serverpath,debugVersion,updateSVN,bundleVersion,packName,channel,sub_channel,APK_PATH,apkName,APK_PATH))
	print "APK unpacked Succeed"
	


	#@rem DLL
	os.system("%s\\MD5Project\\MD5Project.exe DLL %s" % (DLLFiles,DLL_PATH))
	print"SUCCESS encrypt DLL"
	
	if buildDLL== 'true' :
		#@rem copy DLL
		
		os.system("copy /y %s \"%s\" " % (DLL_PATH,finalapkpath))
		print "SUCCESS COPY DLL"
		
		
	else:
		#rem copy libmono.so
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



