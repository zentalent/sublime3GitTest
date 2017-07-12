a = [1,2,3,4]
b = [1]
c = [1]
d = b
e = [1,"hello world",c,False]
f = list("abcd")
print d,b,e,f

a.pop()
a.append(5)
a.index(2)
a[2]
print a,a.index(2)
print (a[0]==b)