while (True):
	filename = raw_input('please input the file name: ')
	try:
		with open (filename) as file_obj:
			contents = file_obj.read()
			print contents
	except IOError:
		print ('check file name or path !')
	else:
		print ('welcome back')