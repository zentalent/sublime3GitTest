def md5(str):
	import hashlib
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()


if md5('') == 'd41d8cd98f00b204e9800998ecf8427e'
	print 'pass'
