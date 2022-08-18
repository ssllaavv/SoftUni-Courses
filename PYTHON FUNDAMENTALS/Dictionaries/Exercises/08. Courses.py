courses_dict = {}

while True:
    input_line = input().split(" : ")
    if input_line[0] == "end":
        break
    course_title = input_line[0]
    student = input_line[1]
    if course_title not in courses_dict:
        courses_dict[course_title] = [student]
    else:  courses_dict[course_title].append(student)


for key, value in courses_dict.items():
    print(f"{key}: {len(value)}")
    for index in range(len(value)):
        print(f"-- {value[index]}")


