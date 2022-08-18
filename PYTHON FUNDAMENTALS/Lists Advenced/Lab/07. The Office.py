employees_happiness = list(input().split())
multiply_factor = int(input())

employees_happiness = list(map(lambda x: int(x) * multiply_factor, employees_happiness))

filtered = list(filter(lambda a: a >= sum(employees_happiness) / len(employees_happiness), employees_happiness))

if len(filtered) >= len(employees_happiness) / 2:
    print(f"Score: {len(filtered)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees_happiness)}. Employees are not happy!")
