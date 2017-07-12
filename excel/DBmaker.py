import os
import xlrd
import sys
import json
from pprint import pprint 

dbPath = "\\\\Server1\\DB\\tk.db"
mysvnPath = "E:\\TankWar1" 
excelPath = mysvnPath + "\\Docs\\ConfTable\\public\\"

# Excel2Sqlite3Prj.exe dbPath=n:\DB\tk.db excelPath=E:\Work\Prj\TankWar1conf_activities_battle_public.xlsx headerRowNum=1 dataRowNum=4 typeRowNum=2 conf_activities_battle

# Exceldict = {}

# if os.path.exists(excelPath) == True :
#  	for file in os.listdir(excelPath):
#  		Exceldict[excelPath+file]=xlrd.open_workbook(excelPath+file).sheets()[0].name

# Exceljson = json.dumps(Exceldict)

sheetlist = open('sheetlist2.json','r+')
exceljson = sheetlist.read()
result = json.loads(exceljson)
sheetlist.close()

sheetlist = open('sheetlist.txt','w')
for key,value in result.items():
	line =str(value)+'.bat'+'\n'
	sheetlist.write(line)
