# Task 1

numbers_list = [int(x) for x in input().split(", ")]
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif number > 5 and number <= 10:
        result /= number

print(result)


# Task 1.2

class ValueCannotBeNegative(Exception):
    """Number is below zero"""
    pass


for _ in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative


# Task 2

word = input('Please, enter a word: ')
while True:
    try:
        times = int(input('Please, enter a number: '))
        break
    except ValueError:
        print('Variable times must be an integer!')
print(word * times)




















