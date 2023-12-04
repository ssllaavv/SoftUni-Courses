# Task 1

import sys

x = int(input())
y = int(input())
z = int(input())


def min_int(a, b, c):

    result = sys.maxsize

    numbers = [a, b, c]

    for n in numbers:
        if n < result:
            result = n

    return result


print(min_int(x, y, z))


# Task 2

def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def ad_and_subtract(a: int, b: int, c: int) -> int:
    x = add(a, b)
    result = subtract(x, c)

    return result


a = int(input())
b = int(input())
c = int(input())

print(ad_and_subtract(a, b, c))


# Task 3

def find_all_characters_inbetween(a: str, b: str) -> str:
    start = ord(a) + 1
    end = ord(b)

    return ' '.join([chr(x) for x in range(start, end)])


x = input()
y = input()

print(find_all_characters_inbetween(x, y))


# Task 4

def odd_and_even_sum(n: str) -> str:
    digits = list(map(int, list(n)))
    evens_sum = sum(list(filter(lambda x: x % 2 == 0, digits)))
    odds_sum = sum(list(filter(lambda x: x % 2 == 1, digits)))

    return f'Odd sum = {odds_sum}, Even sum = {evens_sum}'


number = input()

print(odd_and_even_sum(number))


# Task 5

def filter_evens(line_input: str) -> list[int]:

    numbers_list = list(map(int, line_input.split(' ')))
    filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))

    return filtered_numbers


print(filter_evens(input()))


# Task 6

def sort_numbers(numbers: str):
    numbers_list = list(map(int, numbers.split(' ')))
    sorted_list = sorted(numbers_list)

    return sorted_list


print(sort_numbers(input()))


# Task 7

def find_min_max_and_sum(numbers: str) -> str:
    nums_list = list(map(int, numbers.split(' ')))

    return f"The minimum number is {min(nums_list)}" \
           f"\nThe maximum number is {max(nums_list)}" \
           f"\nThe sum number is: {sum(nums_list)}"


print(find_min_max_and_sum(input()))


# Task 8

def check_if_palindrome(numbers: str):

    numbers_list = numbers.split(', ')
    for n in numbers_list:
        num = list(n)
        reversed_num = list(reversed(num))
        if num == reversed_num:
            print('True')
        else:
            print('False')


check_if_palindrome(input())


# Task 9

def password_validator(password: str):

    is_valid = True

    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False

    digits_count = 0
    for el in password:
        if el.isdigit():
            digits_count += 1

    if digits_count < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")


password_validator(password=input())


# Task 10

def check_if_number_is_perfect(number: int) -> str:

    divisors = []

    for n in range(1, number // 2 + 1):
        if number % n == 0:
            divisors.append(n)

    if sum(divisors) == number:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."


print(check_if_number_is_perfect(int(input())))


# Task 11

def loading_bar(percents: int):
    percent_signs_count = percents // 10
    signs_left = 10 - percent_signs_count

    bar = "%" * percent_signs_count + "." * signs_left

    if percents < 100:
        return f'{percents}% [{bar}]' \
            f'\nStill loading...'
    else:
        return f'100% Complete!' \
               f'\n[%%%%%%%%%%]'


print(loading_bar(int(input())))


# Task 12

def calculate_factorials(number: int):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def calculate_factorials_and_divide(num_1: int, num_2: int):
    return calculate_factorials(num_1) / calculate_factorials(num_2)


n_1 = int(input())
n_2 = int(input())

print(f'{calculate_factorials_and_divide(n_1, n_2):.2f}')

