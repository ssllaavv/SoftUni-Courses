list_of_strings = input().split()
numbers_to_remove = int(input())

list_of_numbers = []
sorted_list = []
final_list = []

for s in list_of_strings:
    list_of_numbers.append(int(s))

sorted_list = list_of_numbers.copy()
sorted_list.sort()

for element in range(numbers_to_remove):
    sorted_list.pop(0)

for element in list_of_numbers:
    if element in sorted_list:
        final_list.append(element)

print(*final_list, sep=", ")
