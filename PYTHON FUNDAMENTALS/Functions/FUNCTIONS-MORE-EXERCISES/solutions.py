# Task 1

def transform_input(input_type: str, input_to_transform: str):
    if input_type == 'int':
        return int(input_to_transform) * 2
    elif input_type == 'real':
        return f"{float(input_to_transform) * 1.5:.2f}"
    elif input_type == 'string':
        return '$' + input_to_transform + '$'


a = input()
b = input()

print(transform_input(a, b))


# Task 2 & Task 3
from math import floor


def find_closer_point(x_1, y_1, x_2, y_2):

    # the distance is the hypotenuse of a ttriangle with sides equal to x and Y coordinates
    # we compare the hypotenuses ** 2 to define the shortest distance, using тхе Pythagorean theorem
    if x_1 ** 2 + y_1 ** 2 <= x_2 ** 2 + y_2 ** 2:
        return floor(x_1), floor(y_1)
    else:
        return floor(x_2), floor(y_2)

# # read the nputs
# x_1 = float(input())
# y_1 = float(input())
# x_2 = float(input())
# y_2 = float(input())
#
# print the result
# print(find_closer_point(x_1, y_1, x_2, y_2))


def find_shorter_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):

    # use the function form Task 1 to find the point proximal to the zero point
    first_line_proximal_point = find_closer_point(x_1, y_1, x_2, y_2)
    if first_line_proximal_point == (floor(x_1), floor(y_1)):
        first_line_distal_point = (x_2, y_2)
    else:
        first_line_distal_point = (x_1, y_1)

    second_line_proximal_point = find_closer_point(x_3, y_3, x_4, y_4)
    if second_line_proximal_point == (floor(x_3), floor(y_3)):
        second_line_distal_point = (x_4, y_4)
    else:
        second_line_distal_point = (x_3, y_3)

    # calculating the cats of to use Pythagorean theorem later, to calculate the length of the lines
    cat_1_1 = first_line_distal_point[0] - first_line_proximal_point[0]
    cat_1_2 = first_line_distal_point[1] - first_line_proximal_point[1]

    cat_2_1 = second_line_distal_point[0] - second_line_proximal_point[0]
    cat_2_2 = second_line_distal_point[1] - second_line_proximal_point[1]

    # comparing lengths of the lines using Pythagorean theorem
    if cat_1_1 ** 2 + cat_1_2 ** 2 >= cat_2_1 ** 2 + cat_2_2 ** 2:
        return f'({floor(first_line_proximal_point[0])}, {floor(first_line_proximal_point[1])})' \
               f'({floor(first_line_distal_point[0])}, {floor(first_line_distal_point[1])})'
    else:
        return f'({floor(second_line_proximal_point[0])}, {floor(second_line_proximal_point[1])})' \
               f'({floor(second_line_distal_point[0])}, {floor(second_line_distal_point[1])})'


# read the inputs
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

# print the result
print(find_shorter_line(x1, y1, x2, y2, x3, y3, x4, y4))


# Task 4

def tribonacci_sequence(n: int):
    if n == 1:
        sequence = [1, ]
    elif n == 2:
        sequence = [1, 1]
    else:
        sequence = [1, 1, 2]
        for i in range(n - 3):
            sequence.append(sum(sequence[-3:]))

    return f'{" ".join(list(map(str, sequence)))}'


number = int(input())

print(tribonacci_sequence(number))


# Task 5

def find_if_result_is_negative_positive_or_zero(x: int, y: int, z: int):
    if any(n == 0 for n in [x, y, z]):
        return 'zero'
    elif len([n for n in [x, y, z] if n > 0]) in [1, 3]:
        return 'positive'
    else:
        return 'negative'


a = int(input())
b = int(input())
c = int(input())

print(find_if_result_is_negative_positive_or_zero(a, b, c))












