# first_number = input("enter your first number: ")
# second_number = input("enter your second number: ")
# total = (int(first_number)*int(second_number))
# print(total)


list = [54,44,27,79,91,41]
list.remove(91)
print(list)
list.insert(2,91)
list.append(91)
print(list)

sample_dict = {'a':100,'b':200,'c':300,'d':400}
print(sample_dict)

if 'b' in sample_dict:
    print("number exists in dictionary")
else:
    print("number does not exist")