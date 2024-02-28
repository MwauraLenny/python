class Employees:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class Receptionist(Employees):
    def __init__(self,name,salary,gender):
       super().__init__(name,salary)
       self.gender = gender
class Frontend_developer(Receptionist):
    def __init__(self,name,salary,gender,programming):
        super().__init__(name,salary,gender)
        self.programming = programming

Receptionist1= Receptionist ('Lenny',200000,'Male')
Employees1 =Employees("Daniel",200000)
programmer =Frontend_developer('Esther','900000','Female','HTML')
print(Receptionist1.name)
print(Employees1.name)
print(programmer.name)
print(programmer.programming)
