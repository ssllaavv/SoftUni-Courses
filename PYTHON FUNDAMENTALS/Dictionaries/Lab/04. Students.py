courses_dict = {}
requested_course_info = ""
while True:
    input_line = input()
    if ":" not in input_line:
        requested_course_info = input_line.split("_")
        break
    values_list = input_line.split(":")
    courses_dict[values_list[0]] = [values_list[1], values_list[2]]

for key, value in courses_dict.items():
    if requested_course_info == (value[1]).split():
        print(f"{key} - {value[0]}")
