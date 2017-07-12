#-*- coding:utf-8 -*-
#用于检测所有装备，强化道具配置的关卡是否有正确掉落

import xlrd
from copy import deepcopy


#stageDict = open("conf_data_dictionary.txt")
#print stageDict.index('BattleName_30101')
conf_drop_publicPath = r'E:\TankWar1\Docs\ConfTable\public\conf_drop_public.xlsx'
conf_props_publicPath = r'E:\TankWar1\Docs\ConfTable\public\conf_props_public.xlsx'
conf_battle_publicPath = r'E:\TankWar1\Docs\ConfTable\public\conf_battle_public.xlsx'

conf_drop_public = xlrd.open_workbook(conf_drop_publicPath)
conf_props_public = xlrd.open_workbook(conf_props_publicPath)
conf_battle_public = xlrd.open_workbook(conf_battle_publicPath)


DropPublic = conf_drop_public.sheets()[0]
PropsPublic = conf_props_public.sheets()[0]
BattlePublic = conf_battle_public.sheets()[0]

DropPublicRows = DropPublic.nrows
PropsPublicRows = PropsPublic.nrows
BattlePublicRows = BattlePublic.nrows


GetDropIDWithLine = {}
GetPropsIDsName = {}
GetBattleIDWithPropID = {}
GetDropIDWithPropID = {}
GetPropsID = []

def GetItemsIDandLine(startID, EndID):
	for itemid in range(startID+5,EndID+6):

		GetDropIDWithLine[itemid]=PropsPublic.row_values(itemid-1)[1]

def GetPropsIDName(lines):
	for line in lines:
		GetPropsIDsName[line]=PropsPublic.row_values(line-1)[3]

def GetBattleID(lines,pos):
	for i in range(lines):
		GetBattleIDWithPropID[GetDropIDWithLine.values()[i]] = PropsPublic.row_values(pos[i]-1)[22:25]
		
def GetDropsItems(line,idNumber):
	GetDropsItem = []
	for item in range(idNumber):
		GetDropsItem.append(DropPublic.row_values(line)[5+item*4])
	return GetDropsItem


def GetRewardID(BattleID):
	
	for i in range(len(BattleID)):
		for j in range(3):
			if BattleID.values()[i][j] == -1.0:
				continue
			else:
				if BattleID.values()[i][j] in range(10101,12022):
					BattleID.values()[i][j]=(BattleID.values()[i][j]-10000)*100+3000000
				elif BattleID.values()[i][j] in range(30101,32021):
					BattleID.values()[i][j]=(BattleID.values()[i][j]-30000)*100+4000000
				# print 'after BattleID[',i,']','[',j,'] = ',(BattleID[i][j]-10000)*100+3000000
	return BattleID

def ToDrop(theid):
	if theid in range(4010100,4202101):
		 theid = (theid-4000000)/100+30000
		 return theid
	else:
		theid = (theid-3000000)/100+10000
		return theid

def checkExist(adict,xlsx,col):
	passcount =0 
	failcount =0
	for i in range (len(adict.keys())):
		for j in range(3):
			for line in range(len(xlsx.col_values(col))):
				if adict.values()[i][j] == -1:
					continue 
				elif xlsx.col_values(col)[line] == adict.values()[i][j]:
						DropIDwithItems = GetDropsItems(line,10)
						if adict.keys()[i] in DropIDwithItems:
							passcount = passcount+1
							# print passcount,'pass:',adict.keys()[i],ToDrop(adict.values()[i][j])
							continue
						else:
							failcount = failcount+1
							print ('!!!Fail-----NO. %s line in file %s ,the item %s is not set in %s %r ' \
							 % (line+1,conf_drop_publicPath,adict.keys()[i],adict.values()[i][j],DropIDwithItems))
	print 'Checked ',passcount+failcount,'items'
	print 'passed',passcount 
	print 'failed',failcount


def findelement(value,col):
	find(value,PropsPublic.raw_values(col))
	return 


if __name__ == "__main__":

	GetItemsIDandLine(31,410)
	GetBattleID(len(GetDropIDWithLine),GetDropIDWithLine.keys())
	GetDropIDWithPropID = deepcopy(GetBattleIDWithPropID)
	GetDropIDWithPropID = deepcopy(GetRewardID(GetDropIDWithPropID))
	checkExist (GetDropIDWithPropID,DropPublic,1)