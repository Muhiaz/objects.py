class Employee():
	def __init__(self,name=input("Enter name: "),regNo=input("Enter regNo: "),gender=input("Enter Gender: ")):
		self.name = name
		self.regNo = regNo
		self.gender = gender
emp1 = Employee('Muhia', 32, 'male')
emp2 = Employee('General', 22, 'male')
emp3 = Employee('Saul', 30, 'female')
print (emp2.name, emp2.gender)
print (emp3.name, emp2.gender)
print (emp1.name, emp2.gender)
emp4 = Employee()