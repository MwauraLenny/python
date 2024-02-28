def my_funtion():
    print('This is my first function')
    print('This is my first function')
    print('This is my first function')
my_funtion()
my_funtion()

def index(name):
    print(name)
    print(name)
    print(name)
index('Lenny')
# index('Mwaura')
# index('Mwangi')

def num(nambari):
    print(nambari)
    print(nambari)
num(18)

def salutation(First_name):
    print('Hi '+First_name +' Good Morning')

salutation('Esther')
salutation('Daniel')

def miaka(age):
    print('Hello, you are '+str(age)+' years old')
miaka(18)

def my_name(first_name , last_name):
    print(first_name+' '+last_name+' is the student')
my_name("Lenny",'Mwaura')

def sentence(first_name,last_name,age):
    print(first_name+' '+last_name+' is '+str(age)+' years old')
sentence('Lenny','Mwaura',18)

def employees(first_name,age):
    if age > 20:
        print(first_name+' you are '+str(age)+' years old')
    elif age <=20 and age >=15:
        print(first_name+' you are '+str(age)+' years old')
    elif age >=10 and age <15:
        print(first_name+' you are '+str(age)+' years old')
    else:
        print(first_name+' you are '+str(age)+' years old.You are too young')
employees('Lenny',18)
employees('Owen',30)
employees('vivian',14)

def age_calculator(age):
    new_age = age+10
    return new_age
print(age_calculator(18))


def marks_calculator(*subjects):
    total = sum(subjects)
    return total
print(marks_calculator(23,45,67))
print(marks_calculator(23,75,45))
print(marks_calculator(79,90))

def exam(first_name,first_test,second_test):
    total = first_name + ' you have acquired a total of ' +str(first_test + second_test)
    return total
print(exam('Lenny',90,76))


def placement(location,age):
    if age > 60:
        print('you have been posted from '+location+ ' to Kisumu')
    elif  age >= 50 and age <=60:
        print('you have been posted from '+location+ ' to Kisumu')
    elif age >= 40 and  age < 50:
        print('you have been posted from '+location+ ' to Kisumu')
    elif age >= 30 and age < 40:
        print('you have been posted from '+location+ ' to Kisumu')
    else:
        print('you have been posted from '+location+ ' to Kisumu')

placement('westlands',35)


def country(nchi ='Kenya'):
    return nchi
print(country('Tanzania'))
print(country('China'))
print(country('Uganda'))
print(country())


