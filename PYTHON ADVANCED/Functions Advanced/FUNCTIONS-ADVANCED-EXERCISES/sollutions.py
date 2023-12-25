# Task 1

def get_numbers_info(nums):
    positives = [n for n in nums if n > 0]
    negatives = list(filter(lambda x: x < 0, nums))
    result = f'{sum(negatives)}\n{sum(positives)}\n'

    if sum(positives) > abs(sum(negatives)):
        result += "The positives are stronger than the negatives"
    elif sum(positives) < abs(sum(negatives)):
        result += "The negatives are stronger than the positives"

    return result


input_line = list(map(int, input().split()))

print(get_numbers_info(input_line))


# Task 2

def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))


# Task 3

def even_odd(*numbers):
    command = list(numbers).pop()
    result = []
    if command == 'even':
        result = [n for n in numbers[: len(numbers) - 1] if n % 2 == 0]
    elif command == 'odd':
        result = [n for n in numbers[: len(numbers) - 1] if n % 2 == 1]

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


# Task 4

def even_odd_filter(**kwargs):
    result = dict()
    for k, v in kwargs.items():
        if k == 'odd':
            values = [n for n in v if n % 2 == 1]
            result[k] = values
        elif k == 'even':
            values = [n for n in v if n % 2 == 0]
            result[k] = values

    result = dict(sorted(result.items(), key=lambda x: -len(x[1])))
    return result


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))


# Task 5

def concatenate(*words, **words_to_replace):
    result = ''
    for w in words:
        result += w
    for word, new_word in words_to_replace.items():
        result = result.replace(word, new_word)

    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))


# Task 6

def func_executor(*args):

    output = ''

    for arg in args:
        f = arg[0]
        result = f(*arg[1])
        output += f'{arg[0].__name__} - {result}\n'

    return output[: len(output) - 1]


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))


# Task 7

def grocery_store(**products):
    output = ''
    result = dict(sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    for k, v in result.items():
        output += f'{k}: {v}\n'
    return output[: len(output) - 1]


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))


# Task 8

def age_assignment(*names, **ages):
    names_and_ages = dict()
    result = ''

    for n in names:
        names_and_ages[n] = ages[n[:1]]

    sorted_names_and_ages = dict(sorted(names_and_ages.items(), key=lambda x: x[0]))
    for name, age in sorted_names_and_ages.items():
        result += f'{name} is {age} years old.\n'

    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


# Task 9

def palindrome(word, index):
    if index == len(word) // 2:
        return f'{word} is a palindrome'

    if word[index] == word[len(word) - 1 - index]:
        return palindrome(word, index + 1)
    else:
        return f'{word} is not a palindrome'


print(palindrome("abcba", 0))
print(palindrome("peter", 0))


# Task 10

def fill_the_box(*args):
    finish_index = args.index('Finish')
    h, l, w = args[:3]
    cubes = args[3: finish_index]
    cubes_volume = sum(cubes)
    volume = h * l * w
    diff = volume - cubes_volume
    if volume > cubes_volume:
        return f'There is free space in the box. You could put {diff} more cubes.'
    else:
        return f'No more free space! You have {abs(diff)} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))


# Task 11

def math_operations(*args, a, s, d, m):
    numbers = list(reversed(args))
    while numbers:
        a += numbers.pop()
        if not numbers:
            break
        s -= numbers.pop()
        if not numbers:
            break
        divisor = numbers.pop()
        if divisor != 0:
            d /= divisor
        if not numbers:
            break
        m *= numbers.pop()

    result = {'a': a,'s': s, 'd': d, 'm': m}
    sorted_result = dict(sorted(result.items(), key=lambda x: (-x[1], x[0])))

    output = ''
    for k, v in sorted_result.items():
        output += f"{k}: {v:.1f}\n"

    return output


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))














