from math import floor

def find_point_closest_to_center(list_of_coordinates):
    abs_list_of_coordinates = list(map(abs, list_of_coordinates))
    min_coordinate = min(abs_list_of_coordinates)
    lowest_index = abs_list_of_coordinates.index(min_coordinate)
    if lowest_index % 2 == 0:
        result = [list_of_coordinates[lowest_index], list_of_coordinates[lowest_index + 1]]
    else:
        result = [list_of_coordinates[lowest_index - 1], list_of_coordinates[lowest_index]]
    return list(map(floor, result))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
coordinates = [x1, y1, x2, y2]
print("(", end="")
print(*find_point_closest_to_center(coordinates), sep=", ", end="")
print(")")




