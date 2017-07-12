import os
import xlrd
import sys
from pprint import pprint 
from collections import Counter

mysvnPath = "E:\\TankWar1" 
excelPath = mysvnPath + "\\Docs\\ConfTable\\public\\"

NullID = 'There is Null value in ID'
DupID = 'ID Duplicated'
NullIDCounter = 0
DupIDCounter = 0

doubleMainKeyExcel =[
'conf_activity_rank_reward_public.xlsx',
# 'conf_airport_reward_public.xlsx',
# 'conf_equip_recast_public.xlsx',
# 'conf_privilege_public.xlsx',
# 'conf_rare_performance_public.xlsx',
'conf_skill_info_public.xlsx'
# 'conf_starstage_public.xlsx',
# 'conf_strategy_arsenal_public.xlsx',
# 'conf_strategy_fortress_public.xlsx',
# 'conf_strategy_researchcenter_public.xlsx',
# 'conf_strategy_zone_link_public.xlsx',
# 'conf_tank_quality_rule_public.xlsx',
# 'conf_vip_buycoin_public.xlsx',
# 'conf_vip_buy_public.xlsx',
# 'conf_weapon_parts_public.xlsx',
# 'conf_weapon_support_public.xlsx'
]



def checkSingleID(issueresult):
	if os.path.exists(mysvnPath) == True :
		for file in os.listdir(excelPath):
			if file not in doubleMainKeyExcel:
				Exceldict = {}
		 		Exceldict[excelPath+file] = xlrd.open_workbook(excelPath+file).sheets()[0].col_values(1)[4:]
		 		if "" in Exceldict.values()[0]:
		 			issueresult[excelPath+file]= NullID
			 	else:
			 		for i in Counter(Exceldict.values()[0]).values():
						if i >1:
							issueresult[excelPath+file]=DupID
							break
						else:
							pass


def NullCheck(issueresult):
	if os.path.exists(mysvnPath) == True :
		for file in os.listdir(excelPath):
			print file
			for i in range(len(xlrd.open_workbook(excelPath+file).sheets()[0].col_values(1)[4:])):
				if "" in xlrd.open_workbook(excelPath+file).sheets()[0].row_values(i)[:]:
					issueresult[excelPath+file] = NullID

		print issueresult

def symbolCheck(issueresult):
	if os.path.exists(mysvnPath) == True :
		for file in os.listdir(excelPath):
			print file
			for i in range(len(xlrd.open_workbook(excelPath+file).sheets()[0].col_values(1)[4:])):
				print type(str(xlrd.open_workbook(excelPath+file).sheets()[0].cell_value(i+4,0)))
				if str(xlrd.open_workbook(excelPath+file).sheets()[0].cell_value(i+4,0)).isspace() :
						 issueresult[excelPath+file] = 'empty'
		print issueresult


def outputWrongSheets(issueresult,NullIDCounter,DupIDCounter):
		NullIDList = []
		DupIDList = []
		for key,value in issueresult.items():
			if value == NullID:
				NullIDList.append(key)
				NullIDCounter = NullIDCounter + 1
			elif value == DupID:
				DupIDList.append(key)
				DupIDCounter = DupIDCounter + 1 
		print "-------There are ",NullIDCounter,"sheets with null value in ID------- "
		pprint (NullIDList)
		print "-------There are ",DupIDCounter, "sheets with duplicated values in ID-------"
		pprint (DupIDList)


def checkDoubleID():
	for file in doubleMainKeyExcel:
		Exceldict={}
		Exceldict[excelPath+file] = [xlrd.open_workbook(excelPath+file).sheets()[0].col_values(1)[4:],xlrd.open_workbook(excelPath+file).sheets()[0].col_values(2)[4:]]
		# for key,values in Counter(Exceldict.values()[0][0]).items():
		# 	for i in range(len(Counter(Exceldict.values()[0][0]).items())):
		# 		print i
		# 		print Exceldict.values()[0][0][Exceldict.values()[0][0].index(key):values*(i+1)]
		dup = []
		for i in range(len(Counter(Exceldict.values()[0][0]).keys())):
			print len(Counter(Exceldict.values()[0][0]).keys())			
			
			j=Exceldict.values()[0][1]\
			[Counter(Exceldict.values()[0][0]).values()[i]*i:(i+1)*Counter(Exceldict.values()[0][0]).values()[i]]
			print file,j
			i = Counter(j).values()
			if i >1:
				print i 

				

	print issueresult


if __name__ == "__main__":

	issueresult = {}
	NullIDCounter = 0
	DupIDCounter = 0
	# checkSingleID(issueresult)
	# if issueresult > 0:
	# 	outputWrongSheets(issueresult,NullIDCounter,DupIDCounter)
	# else:
	# 	print "Good Everything is OK"
	# checkDoubleID()
	checkDoubleID()


	
	
