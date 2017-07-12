
import pprint
import svn.local
import os

	


r = svn.local.LocalClient("E:\TankWar1")
info = r.info()
print info['commit#revision']
pprint.pprint(info)


def findapkname(apkpath):
	for a in os.listdir(apkpath):
		if os.path.isfile(a) == False:
			return os.path.splitext(a)[0]

path = "E:\DLLFiles\Version"
print findapkname(path)
print os.path.isdir(path)


