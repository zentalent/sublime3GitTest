# -*- coding: utf-8 -*-
# -*- coding: gbk -*-
#coding = gbk
import os
import sys
import re

def getPackInfoToConsole(Apkname):
	return os.system('aapt dump badging '+Apkname)

def getPackInfoToFile(Apkname,filename):
	return os.system('aapt dump badging '+Apkname +'>'+filename)

def launchGame(packname,launchname):
	
	os.system('adb shell am start -n '+packname+'/'+ launchname)
	print 'now start the game'
	
def installPack(apk):
	print 'now install the pack'
	os.system('adb install -r '+ apk)
	print 'installed'
	
def resetAdb():
	os.system('adb kill-server')
	
def stopGame(packname):
	os.system('adb shell am force-stop '+packname)
	
def logtrack():
	os.system('adb locat 10 *:D')
	
apkfilename = "Tank_trunktest_1.3.44174_channel3_304.apk"
tempfilename = "temp"
finalapkpath = "\\\\Server1\\开发存档（正式）\\Version\\正式包\\android\\".decode('utf-8').encode('gbk')
print type(finalapkpath)
apkname = finalapkpath + apkfilename


f = open(tempfilename,'r')
fstr = f.read()
f.close()
packname = str(re.search("(?<=package: name=').*(?=' versionCode=)",fstr).group())
launchname = str(re.search("(?<=launchable-activity: name=').*(?='  label=')",fstr).group())


#检测配置环境
#找到目标安装包

#找到安装包的包名和启动名称
#将包安装到目标机器
#安装成功后启动
#自动运行
#卸载