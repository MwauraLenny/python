# no.1

# age = int(input("how old are you? "))
# if age >=18:
#     print("you are old enough to move out")
#     print("you are old enough to have an ID")
# else:
#     print("you are too young to move out")
#     print("you are not valid for an ID")


# no.2

# marks = float(input("Enter your Marks: "))
# if marks >=80 and marks<=100:
#     print("you have an A")
#
# elif marks >=60 and marks <=79:
#     print("you have a B")
#
# elif marks >= 50 and marks <= 69:
#     print("you have a C")
#
# elif marks >= 40 and marks <= 49:
#     print("you have a D")
#
# elif marks >= 0 and marks <= 39:
#     print("you have an E")
#
# else:
#     print("Enter valid marks (0 - 100)")


# no.3

# age = int(input("how old are you? "))
# if age >65:
#     print("you are old enough to retire")
# elif age >65 and age >=50:
#     print("you are almost going to retire")
# elif age >50 and age >=40:
#     print("you are still active")
# elif age <40 and age >=18:
#     print("you are considered youthful")
# else:
#     print("you are still young")


# temp = float(input("what is your body temperature? "))
# if temp >30:
#     print("please wear only a vest")
# elif temp >=20 and temp <30:
#     print("you should wear a sweater")
# else:
#     print("put on a jacket")
#

H = float(input("What is your height in meters? "))
W = float(input("What is your weight in kilograms? "))
BMR = W/(H*H)
print("your BMI is this")
print(BMR)
if BMR < 18:
    print("you are underweight")
elif BMR > 18 and BMR <=25:
    print("you are normal")
elif BMR >25  and BMR <=30:
    print("you are overweight")
elif BMR >30:
    print("you are obese")
else:
    print("Enter valid values")






