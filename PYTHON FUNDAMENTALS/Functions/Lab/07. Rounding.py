def rounder(num_list):
    list_of_rounded_numbers = []
    for element in num_list:
        rounded_element = round(float(element))
        list_of_rounded_numbers.append(rounded_element)
    return list_of_rounded_numbers


input_line = input().split()
result = rounder(input_line)
print(result)



