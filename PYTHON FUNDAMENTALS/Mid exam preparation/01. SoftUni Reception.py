from math import ceil
efficiency_first = int(input())
efficiency_second = int(input())
efficiency_third = int(input())
students_count = int(input())

total_efficiency = efficiency_first + efficiency_second + efficiency_third
time = ceil(students_count / total_efficiency)
if time % 3 != 0:
    time = time + (time // 3)
else:
    time = time + (time // 3) - 1

print(f"Time needed: {time}h.")