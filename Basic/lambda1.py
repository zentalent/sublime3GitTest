def func(a,b,c):
	return a+b+c

print func(1,2,3)


print (lambda a,b,c:a+b+c)(1,2,3)

(lambda :print 'this is a lambda')