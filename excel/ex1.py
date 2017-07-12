import os
import xlrd

try:

	conf_battle_publicPath = r'E:\TankWar1\Docs\ConfTable\public\conf_battle_publc.xlsx'
	# if os.path.exists(conf_battle_publicPath) == False:
	# 	raise Exception("Wrong DIR",conf_battle_publicPath)
except IOError:
	print conf_battle_publicPath
else:
	conf_battle_public = xlrd.open_workbook(conf_battle_publicPath)
	print 'good'

