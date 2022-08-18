from math import floor

def find_closest_coordinates_to_zero(x_1, y_1, x_2, y_2):
    distance_first_point = (abs(x_1) ** 2 + abs(y_1) ** 2) ** (1 / 2)
    distance_second_point = (abs(x_2) ** 2 + abs(y_2) ** 2) ** (1 / 2)
    if distance_second_point >= distance_first_point:
        result = f"({floor(x_1)}, {floor(y_1)})"
    else:
        result = f"({floor(x_2)}, {floor(y_2)})"
    return result

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(find_closest_coordinates_to_zero(x1, y1, x2, y2))
