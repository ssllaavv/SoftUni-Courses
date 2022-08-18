first_eff = int(input())
second_eff = int(input())
third_eff = int(input())
students_count = int(input())

time = 0
total_eff = first_eff + second_eff + third_eff

while students_count > 0:
    if time != 0 and (time + 1) % 4 == 0:
        time += 1
    students_count -= total_eff
    time += 1

print(f"Time needed: {time}h.")
