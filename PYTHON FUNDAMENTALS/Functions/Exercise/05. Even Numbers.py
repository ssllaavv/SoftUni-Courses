list_of_numbers = input().split()
list_of_numbers_int = []
for element in list_of_numbers:
    list_of_numbers_int.append(int(element))

filtered = filter(lambda even: even % 2 == 0, list_of_numbers_int)
print(list(filtered))
