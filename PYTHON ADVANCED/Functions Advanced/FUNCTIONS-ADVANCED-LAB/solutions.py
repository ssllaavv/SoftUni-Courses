# # Test 1
#
# def calculate(operator):
#     def addition(a, b):
#         return a + b
#
#     def subtraction(a, b):
#         return a - b
#
#     if operator == '-':
#         return subtraction
#     elif operator == '+':
#         return addition
#
#
# print(calculate('-')(1, 3))


# # Test 2
#
# def outside_function(number):
#     def inside_function():
#         return number
#     return inside_function
#
#
# print(outside_function(10)())


# # Test 3
#
# def greeting(name):
#     hello = "Hello, "
#
#     def say_hi():
#         return hello + name
#     return say_hi()
#
#
# print(greeting("Peter"))


# # Test 4
#
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact
#
#
# print(factorial(4))


# # Test 5
#
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(4))


# Task 1

def multiply(*nums):
    result = 1
    for n in nums:
        result *= n
    return result


# print(multiply(3, 4))


# Task 2

def get_info(name, age, town):
    return f'This is {name} from {town} and he is {age} years old'


# person = {"name": "George", "town": "Sofia", "age": 20}
# print(get_info(**person))


# Task 3

def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for k, v in sorted_cheeses:
        result += k + '\n'
        for q in sorted(v, reverse=True):
            result += str(q) + '\n'
    return result[: len(result) - 1]


# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )
#
# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )


# Task 4
def rectangle(a, b):
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        return "Enter valid values!"

    def area():
        return a * b

    def perimeter():
        return 2 * a + 2 * b

    return f"Rectangle area: {area()}\n" \
           f"Rectangle perimeter: {perimeter()}"


# print(rectangle(2, 10))


# Task 5

def recursive_power(num, power):
    if power == 1:
        return num
    return num * recursive_power(num, power - 1)


# print(recursive_power(2, 3))

























