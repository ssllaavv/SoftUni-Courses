def two_numbers_factorial_division(num1, num2):
    factorial_of_num1 = 1
    factorial_of_num2 = 1
    for n1 in range(1, num1 + 1):
        factorial_of_num1 *= n1
    for n2 in range(1, num2 + 1):
        factorial_of_num2 *= n2
    return factorial_of_num1 / factorial_of_num2

first_number = int(input())
second_number = int(input())

result = two_numbers_factorial_division(first_number, second_number)
print(f"{result:.2f}")


