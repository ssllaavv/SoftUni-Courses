def find_smallest_num(num1, num2, num3):
    list_numbers = [num1, num2, num3]
    smallest_num = min(list_numbers)
    return smallest_num

first_number = int(input())
second_number = int(input())
third_number = int(input())

result = find_smallest_num(first_number, second_number, third_number)
print(result)
