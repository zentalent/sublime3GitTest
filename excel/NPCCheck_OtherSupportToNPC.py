import os
import xlrd
import sys
from pprint import pprint 
from collections import Counter
from sys import argv
import svn.local

p,PROJECT_PRJPATH,updateSVN = argv
mysvnPath = PROJECT_PRJPATH
excelPath = mysvnPath + "\\Docs\\ConfTable\\"

Conf_npc_tank= xlrd.open_workbook(excelPath+'public\\conf_npc_tank_public.xlsx').sheets()[0]
Conf_battle_other_support = xlrd.open_workbook(excelPath+'client\\conf_battle_other_support_client.xlsx').sheets()[0]


NPClist = []
enemy_tank_list_ofOtherSupport = []
enemy_support_tank_list_ofOtherSupport = []

for i in Conf_npc_tank.col_values(1)[4:]:
	NPClist.append(str(int(i)))


for i in Conf_battle_other_support.col_values(6)[4:]:
	i = str(i).split(',')
	#print i
	for j in range(len(i)):
		#print len(i)
		#print i[j]
		if i[j] == '-1' :
			pass
		elif i[j] not in NPClist:
			print i
			print i[j],'is not in NPC sheet'

for i in Conf_battle_other_support.col_values(7)[4:]:
	i = str(i)
	if i == '-1' or i =='-1.0':
		pass
	else:
		enemy_support_tank_list_ofOtherSupport.append(i.split('|')[1])
		

for i  in enemy_support_tank_list_ofOtherSupport:
	i = str(i).split(',')
	for j in range(len(i)):
		# print i[j]
		if i[j] == '-1':
			pass
		elif i[j] not in NPClist:
			print i
			print i[j],'is not in NPC sheet'