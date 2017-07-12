class Employee:
	'All Employee Base Class'
	empCount = 0 

	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1


	def displayCount(self):
		print "Total Employee %d" % Employee.empCount

	def displayEmployee(self):
		print "Name : ",self.name,",Salary: ",self.salary


if __name__ == "__main__":
	obj = Employee('GG',10)
	obj.displayCount()
	obj.displayEmployee()
print ''
print Employee.__doc__
print Employee.__name__
print Employee.__module__
print Employee.__bases__
print Employee.__dict__