def sum_numbers(a, b):
    return a + b

def subtract (sum_num, c):
    return sum_num -c

def sum_and_subtract(x, y, z):
    sum_of_two_integers = sum_numbers(x, y)
    result = subtract(sum_of_two_integers, z)
    return result

first_num = int(input())
second_num = int(input())
third_num = int(input())
print(sum_and_subtract(first_num, second_num, third_num))