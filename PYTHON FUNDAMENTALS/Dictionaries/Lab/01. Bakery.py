input_list = input().split()
products_dict = {}
for el in range(0, len(input_list), 2):
    key = input_list[el]
    value = input_list[el+1]
    products_dict[key] = int(value)
print(products_dict)



