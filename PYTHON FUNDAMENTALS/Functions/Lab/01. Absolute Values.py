
numbers = input().split()
list_of_numbers = []
for element in numbers:
    number = float(element)
    list_of_numbers.append(number)
list_of_abs = []
for num in list_of_numbers:
    abs_num = abs(num)
    list_of_abs.append(abs_num)
print(list_of_abs)




