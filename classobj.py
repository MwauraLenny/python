class Person:
    name = 'Lenny'
    age = 18
    gender = 'male'
    marital_status = 'married'
print(Person.name)
print(Person.age)
print(Person.gender)
print(Person.marital_status)
Person.age = 20
print(Person.age)

class Employees:
    first_name ='Lenny'
    last_name = 'Mwaura'
    Salary = 100000
    Age = 20
    gender = 'male'
print(f"{Employees.first_name} {Employees.last_name} your age is {Employees.Age} and you earn a salary of {Employees.Salary} and you are of gender {Employees.gender} ")
print(f"{Employees.last_name} you are a {Employees.gender}")
print(f"{Employees.first_name} is a {Employees.gender} of age {Employees.Age}")


class Parent:
    first_name = 'Lenny'
    last_name = 'Mwangi'
parent1 = Parent()
print(parent1.first_name)
print(parent1.last_name)

class Parent:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age  = age
parent1 = Parent('Lenny','Mwaura',18)
parent2 = Parent('Daniel','Mwangi',45)
parent3 = Parent('Esther','Wachiuri',40)
print(parent1.first_name)
print(parent2.first_name)
print(parent3.first_name)
print(parent1.last_name)
print(parent2.last_name)
print(parent3.last_name)
print(parent1.age)
print(parent2.age)
print(parent3.age)

class Cars:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
car1 = Cars('Ford','Ranger',2000)
car2 = Cars('Mercedes','Benz',2015)
car3 = Cars('Bugatti','Veron',2013)
print(car1.make)
print(car2.make)
print(car3.make)
print(f"My car is a {car1.make} {car1.model} manufactured in the year {car1.year}")
print(f"{car1.make},{car2.make} and {car3.make} were all manufactured in the year  {car1.year}")

class Students:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname =lastname
        self.age = age
student1 =Students ('Lenny','Mwaura',18)
student2 =Students ('Daniel','Mwangi',20)
student3 =Students ('Lawrence','Wachiuri',14)
print(f"{student1.firstname} {student1.lastname} graduated top of his class in high school,he is {student1.age} years old.")
print(f"{student2.firstname} {student2.lastname} was second yet is his {student2.age} years old.")
print(f"On the other hand,{student3.firstname} {student3.lastname} completed third even though he is {student3.age} years old. ")

class Magari:
    def __init__(self,make,model,price,year):
        self.make = make
        self.model = model
        self.price = price
        self.year = year
    def describe(self):
        print(f"My favourite car is {self.model} and it is a model of {self.make} and it costs {self.price}.it was made in the year {self.year} ")

obj1 = Magari('Ford','Ranger',2000000,2018)
obj2 = Magari('Mercedes','Benz',2100000,2019)
obj3 = Magari('Bugatti','Veron',1400000,2016)

obj1.describe()
obj2.describe()
print(obj3.describe())

class Person:
    def __init__(self,firstname,lastname,gender,age):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
    def describe(self):
        print(f"The student's name is {self.firstname} {self.lastname} of gender {self.gender} and is {self.age} years old.")
student1 = Person('Lenny','Mwaura','male',18)
student2 = Person('Daniel','Mwangi','male',26)
student3 = Person('Esther','Wachiuri','female',24)

print(student1.describe())
print(student2.describe())
print(student3.describe())

class Person:
    def __init__(self,firstname,lastname,gender,age):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
    def fullname(self):
        print(f"{self.firstname} {self.lastname}")
    def display_age(self):
        print(self.age)
    def display_gender(self):
        print(self.gender)
    def increament_age(self):
        self.age +=10
        # or self.age =self.age + 10

student1 = Person('Lenny','Mwaura','male',18)
student2 = Person('Daniel','Mwangi','male',26)
student3 = Person('Esther','Wachiuri','female',24)

(student1.fullname())
(student2.display_age())
(student1.display_age())
student1.increament_age()
print(student1.display_age())
