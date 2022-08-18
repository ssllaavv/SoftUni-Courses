students_grade_dict = {}
final_dict = {}
input_pairs = int(input())

for s in range(input_pairs):
    name = input()
    grade = float(input())
    if name not in students_grade_dict:
        students_grade_dict[name] = [grade]
    else:
        students_grade_dict[name].append(grade)

sum_of_grades = 0
for student, grade in students_grade_dict.items():
    for value in grade:
        sum_of_grades += value
    average_grade = sum_of_grades / len(grade)
    if average_grade >= 4.5:
        final_dict[student] = average_grade
    sum_of_grades = 0

for student, grade in final_dict.items():
    print(f"{student} -> {grade:.2f}")


