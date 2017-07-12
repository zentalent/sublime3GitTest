# -*- coding: utf-8 -*-
# -*- coding: gbk -*-
#coding = gbk
import sys
from sys import argv
import svn.local
import os
reload(sys)
sys.setdefaultencoding("utf-8")

channelId = '1'
PROJECT_PRJPATH = 'E:\TankWar1'


UnityPath = 'C:\Program Files\Unity\Editor\Unity.exe'
bundleIdentifier = 'E:\DLLFiles\Version'
serverpath = 'com.tencent.tmgp.fxzjxx'
updateSVN = 'ceshifu$http://192.168.20.201:8080/GatewayServer/game/ProtoReceiver'
debugVersion = 'false'
bundleVersion = '1.3.44076'
packName = '44306'
channel = '3$壕鑫'
sub_channel = '301$MAIN'
DLLFiles ="E:\DLLFiles"
APK_PATH = DLLFiles+"\\Version"
LogPath = DLLFiles+"\\LogFile\\buildAPK_Main.txt"
svnVersion = '44380'


print os.system("del /f/s/q %s\Assets\Plugins\Android\*.aar" % PROJECT_PRJPATH)
print os.system("copy /y %s\\Data\\Channel\\%s\\*.* %s\\Assets\\Plugins\\Android" % (PROJECT_PRJPATH,channelId,PROJECT_PRJPATH))
def pack():

	os.system('call "%s" -logfile "%s" -quit -batchmode -projectPath "%s" -executeMethod BuildCommand.BuildAndroid start %s %s %s %s %s %s "" %s %s %s end '\
		% (UnityPath,LogPath,PROJECT_PRJPATH,APK_PATH,bundleIdentifier,serverpath,debugVersion,bundleVersion,packName,svnVersion,channel,sub_channel))
print "start packing"

packres = pack()
if packres != 0:
	print "packing......"
else:
	print "finished"
