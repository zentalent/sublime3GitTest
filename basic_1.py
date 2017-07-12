bicycles = ['trek','cannondale','redline','specialized']
car = ['benz','bmw','Audi']
bicycles.append(car)
del bicycles[0]
print bicycles

popped_bicycle = bicycles.pop()
print bicycles
print popped_bicycle

bicycles.remove('redline')
print bicycles 
