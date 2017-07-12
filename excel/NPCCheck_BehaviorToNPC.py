import os
import xlrd
import sys
from pprint import pprint 
from collections import Counter
from sys import argv

p,PROJECT_PRJPATH,updateSVN = argv
mysvnPath = PROJECT_PRJPATH
excelPath = mysvnPath + "\\Docs\\ConfTable\\"

Conf_battle_behavior = xlrd.open_workbook(excelPath+'client\\conf_battle_behavior_client.xlsx').sheets()[0]
Conf_npc_tank= xlrd.open_workbook(excelPath+'public\\conf_npc_tank_public.xlsx').sheets()[0]
Conf_battle_other_support = xlrd.open_workbook(excelPath+'client\\conf_battle_other_support_client.xlsx').sheets()[0]

Dict_battle_behavior={}

NPClist = []
enemy_support_tank_list_ofBehavior = []

Dict_battle_behavior [excelPath+'client\\conf_battle_behavior_client.xlsx']= \
[Conf_battle_behavior.col_values(18)[4:],Conf_battle_behavior.col_values(19)[4:]]


for i in Conf_npc_tank.col_values(1)[4:]:
	NPClist.append(str(int(i)))
#print NPClist

for i in Dict_battle_behavior.values()[0][0]:
	i = str(i).split(',')
	#print i
	for j in range(len(i)):
		#print len(i)
		#print i[j]
		if i[j] == '-1' :
			pass
		elif i[j] not in NPClist:
			print i[j],'is not in NPC sheet'


for i in Dict_battle_behavior.values()[0][1]:
	i = str(i)
	if i == '-1' or i =='-1.0':
		pass
	else:
		enemy_support_tank_list_ofBehavior.append(i.split('|')[1])
		

for i  in enemy_support_tank_list_ofBehavior:
	i = str(i).split(',')
	for j in range(len(i)):
		# print i[j]
		if i[j] == '-1':
			pass
		elif i[j] not in NPClist:
			print i
			print i[j],'is not in NPC sheet'
			