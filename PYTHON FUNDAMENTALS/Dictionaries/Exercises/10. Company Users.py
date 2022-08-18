employee_dict = {}

while True:
    input_line = input().split(" -> ")
    if input_line[0] == "End":
        break
    company = input_line[0]
    employee_id = input_line[1]
    if company not in employee_dict:
        employee_dict[company] = [employee_id]
    else:
        if employee_id not in employee_dict[company]:
            employee_dict[company].append(employee_id)

for company, ids in employee_dict.items():
    print(company)
    for id in ids:
        print(f"-- {id}")
