def find_multiplication_result_range(x, y, z):
    if (x < 0 and y < 0 and z < 0) or \
            (x < 0 and y > 0 and z > 0) or \
            (x > 0 and y < 0 and z > 0) or \
            (x > 0 and y > 0 and z < 0):
        print("negative")
    elif x == 0 or y == 0 or z == 0:
        print("zero")
    else:
        print("positive")

first_num = int(input())
second_num = int(input())
third_num = int(input())
find_multiplication_result_range(first_num, second_num, third_num)
