# Task 1

list_of_strings = input().split(' ')

list_of_numbers = []
list_of_absolute_numbers = []

for el in list_of_strings:
    num = float(el)
    list_of_numbers.append(num)

for num in list_of_numbers:
    abs_num = abs(num)
    list_of_absolute_numbers.append(abs_num)

print(list_of_absolute_numbers)


# Task 2

g = float(input())


def solve(grade: float):

    result = ''

    if 2.00 <= grade <= 2.99:
        result = 'Fail'
    elif 3.00 <= grade <= 3.49:
        result = 'Poor'
    elif 3.50 <= grade <= 4.49:
        result = 'Good'
    elif 4.50 <= grade <= 5.49:
        result = 'Very Good'
    elif 5.50 <= grade <= 6.00:
        result = 'Excellent'

    print(result)


solve(g)


# Task 3

operation = input()
first_num = int(input())
second_num = int(input())


def calculate(num_1: int, num_2: int, operator: str) -> float:
    result = None

    if operator == 'multiply':
        result = num_1 * num_2

    elif operator == 'divide':
        result = num_1 / num_2

    elif operator == 'add':
        result = num_1 + num_2

    elif operator == 'subtract':
        result = num_1 - num_2

    return round(result)


print(calculate(first_num, second_num, operation))


# Task 4

string = input()
num = int(input())

result = lambda s, n: s * n
print(result(string, num))


# Task 5

product = input()
quantity = int(input())


def order_price(prod: str, qtt: int) -> float:
    price = 0

    if prod == 'coffee':
        price = 1.5
    elif prod == 'water':
        price = 1
    elif prod == 'coke':
        price = 1.4
    elif prod == 'snacks':
        price = 2

    total_price = price * qtt

    return total_price


print(f'{order_price(product, quantity):.2f}')


# Task 6 = solution 1

def calculate_rectangle_area(x: int, y: int) -> int:
    return x * y


print(calculate_rectangle_area(int(input()), int(input())))


# Task 6 = solution 2

length = int(input())
height = int(input())

area = lambda x, y: x * y

print(area(length, height))


# Task 7

def round_the_numbers(single_line_of_numbers_input: str) -> list:
    numbers = list(map(float, single_line_of_numbers_input.split(' ')))
    return list(map(round, numbers))


print(round_the_numbers(input()))


