my_list = [1, 3, 2, 4, 2, 5, 6, 2,  7, 8, 9]

another_list = ["Gosho", "Slavi", "Petar", "Anastasia"]

another_list.pop()
another_list.sort()
another_list.insert(0, "Anastasia")
print(another_list)

number = another_list.index("Slavi")
#while 2 in my_list:
#    my_list.remove(2)

print(my_list.count(2))
del my_list[4]
print(my_list[::-1])


