list_of_strings = input().split()
numbers_to_remove = int(input())
list_of_numbers = []
final_list = []
for s in list_of_strings:
    list_of_numbers.append(int(s))
final_list = list_of_numbers.copy()
for remove in range(numbers_to_remove):
    final_list.remove(min(final_list))

print(*final_list, sep=", ")
