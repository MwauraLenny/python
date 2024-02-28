my_set = {122,345,643,784,786,476,463,976,567}
print(my_set)


my_set.add(457)
print(my_set)
my_set.update([678,123,345,729,906])
print(my_set)


my_set2 = my_set.copy()
print(my_set2)

print(len(my_set))
my_set.discard(786)
print(my_set)
my_set.clear()
print(my_set)

del my_set
print(my_set2)

print(max(my_set2))
print(min(my_set2))
print(sum(my_set2))
print(sum(my_set2)/len(my_set2))

names = {'Lenny','Peter','Maranda','Daniel','Josh'}
print(names)
if 'Lenny'in names:
    print("Student is present in the school system")
else:
    print("Student is not present in the school system")


parents = {'Daniel','Esther','Mwaura','Mwangi','Wachiuri','Wairimu'}
one_value = 'Mwangi'
if one_value in parents:
    output = one_value
    print(output)

test = {12,46,67,36,89.0,42.6,83.7}
print(test)
number = 12
if number in test:
    answer = number
    print(answer)

number = 46
if number in test:
    answer = number
    print(answer)

number = 42.6
if number in test:
    answer = number
    print(answer)

number = 89.0
if number in test:
    answer = number
    print(answer)
