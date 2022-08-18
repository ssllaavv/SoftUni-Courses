from math import floor

def find_the_longer_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    x_first = x_2 - x_1
    y_first = y_2 - y_1
    x_second = x_4 - x_3
    y_second = y_4 - y_3
    first_line_length = (abs(x_first) ** 2 + abs(y_first) ** 2) ** (1 / 2)
    second_line_length = (abs(x_second) ** 2 + abs(y_second) ** 2) ** (1 / 2)
    if first_line_length >= second_line_length:
        result = f"({floor(x_2)}, {floor(y_2)})({floor(x_1)}, {floor(y_1)})"
    else:
        result = f"({floor(x_4)}, {floor(y_4)})({floor(x_3)}, {floor(y_3)})"
    return result

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(find_the_longer_line(x1, y1, x2, y2, x3, y3, x4, y4))
