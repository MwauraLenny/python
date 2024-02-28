 # list
my_list = [123,276,356,354,782]
print(my_list)
print(my_list[3])
print(my_list[0])
print(my_list[4])

print(my_list[1:4])

my_list[0] = 132
print(my_list)
my_list[4] =567
print(my_list)

print(len(my_list))

my_list.append(434)
print(my_list)
my_list.insert(1,254)
print(my_list)
my_list.insert(4,690)
print(my_list)
my_list.extend([234,654,789])
print(my_list)

my_list.remove(276)
print(my_list)
del my_list[4]
print(my_list)
print(len(my_list))

my_list.clear()
print(my_list)

del my_list

my_list2 = [134,452,354,457,765,647,765,248,978]
print(max(my_list2))
print(min(my_list2))
print(sum(my_list2))
print(sum(my_list2)/len(my_list2))

print(my_list2.index(457))

del my_list2

my_list3 = ['Lenny','Mwaura','Mwangi','Daniel','Lawrence']
print(my_list3)
my_list3.append('Esther')
print(my_list3)
del my_list3[0]
print(my_list3)

del my_list3




