a = {'Tom' : 8 , "Jack":7}
print a

b = dict (Tom = 8, Jerry = 7)
print b

c = a.get('Jack')
print c

a['Spike'] = 6
a['Tyke'] = 5
a.update({'Tuffy':2,"Mashoe":4})
print (a)

for k in a:
	print k