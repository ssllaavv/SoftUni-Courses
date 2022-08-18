def print_sorted_ints(list_as_stings):
    list_of_numbers_as_int = []
    sorted_list = []
    for element in list_as_stings:
        list_of_numbers_as_int.append(int(element))
    sorted_list = sorted(list_of_numbers_as_int.copy())
    print(sorted_list)

list_of_numbers_as_strings = input().split()
print_sorted_ints(list_of_numbers_as_strings)
