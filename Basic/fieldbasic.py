def mygenerator():
	print ' start ...'
	yield 5
	print 'doing'
	yield 20
	print 'end'
	yield 30

g1 =mygenerator()
g1.next()