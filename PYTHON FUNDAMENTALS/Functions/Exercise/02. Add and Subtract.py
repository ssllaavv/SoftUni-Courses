def sum_of_first_two_numbers(num1, num2):
    return num1 + num2

def subtract_third_num_from_sum_result(result_sum, num3):
    return result_sum - num3

first_number = int(input())
second_number = int(input())
third_number = int(input())

result_sum = sum_of_first_two_numbers(first_number, second_number)
print(subtract_third_num_from_sum_result(result_sum, third_number))
