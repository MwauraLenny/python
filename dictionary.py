my_dictionary ={
    "Name": "Lenny",
    "Gender":"Male",
    "Age":18,
    "Marital Status":"Married"
}
# specific info
print(my_dictionary)
print(my_dictionary["Marital Status"])
print(my_dictionary["Name"])
print(my_dictionary["Gender"])
# or
print(my_dictionary.get("Gender"))

# editing
my_dictionary["Marital Status"] = "single"
print(my_dictionary["Marital Status"])
my_dictionary["Age"] = 20
print(my_dictionary["Age"])

# inserting elements
my_dictionary["location"] = "Westlands"
print(my_dictionary)
my_dictionary["salary"] = 200000
print(my_dictionary["salary"])

my_dictionary2 = my_dictionary.copy()
print(my_dictionary2)
print(len(my_dictionary2))

my_dictionary.pop("Name")
print(my_dictionary)
my_dictionary.pop("Marital Status")
print(my_dictionary)
del my_dictionary["Gender"]
print(my_dictionary)
my_dictionary.clear()
print(my_dictionary)
del my_dictionary
print(my_dictionary2)

car = {
    "name":"Rav 4",
    "color":"grey",
    "Model":"type 3",
    "age":"9yrs",
    "owner":"Daniel",
    "origin":"japan",
    "year of creation":"2015"
}
print(car)
