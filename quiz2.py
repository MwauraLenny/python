def student(firstname,lastname,age):
    print(firstname +' '+ lastname +' ' +' is a univerity student of age '+str(age))
student('Lenny','Mwaura',18,)

class Student:
    def __init__(self,student_name,marks):
        self.student_name = student_name
        self.marks = marks
student1 =Student ('Daniel',93)
print(student1.student_name)
print(student1.marks)
student1.student_name = 'Esther'
student1.marks = 90
print(student1.student_name)
print(student1.marks)

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.area = length * width

rect1 = Rectangle (30,10)
print(rect1.length)
print(rect1.width)
print(rect1.area)


class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.perimeter =(22/7)*(radius*2)
        self.area = (22/7) * (radius*radius)
circle =Circle(30)
print(circle.radius)
print(circle.area)
print(circle.perimeter)

class Bank_account:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number =account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    def deposit(self):
        deposit=int(input("enter amount to deposit: "))
        balance = self.balance + deposit
        print(f"your have a balance of {balance}")
    def withdraw(self):
       withdraw = int(input("Enter amount you wish to withdraw"))
       balance = self.balance - withdraw
       print(f"your new balance is {balance}")

customer1 = Bank_account(1030345,350000," 20 dec 2015","Lenny Mwaura")
customer1.withdraw()
customer1.deposit()





























