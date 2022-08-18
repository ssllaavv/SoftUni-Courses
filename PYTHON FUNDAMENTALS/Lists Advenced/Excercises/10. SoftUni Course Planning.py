plan = input().split(", ")
command = input().split(":")

while command != ['course start']:
    operation = command[0]
    lesson_title = command[1]
    if operation == "Add":
        pass
    elif operation == "Insert":
        pass
    elif operation == "Remove":
        pass
    elif operation == "Swap":
        pass
    elif operation == "Exercise":
        for element in plan:
            if lesson_title in element:
                if lesson_title == element:
                    lesson_index = plan.index(element)
                    if lesson_title not in plan[lesson_index + 1]:
                        plan.insert(lesson_index + 1, (f"{lesson_title}-Exercise"))
                else:
                    exercise_index = plan.index(element)
                    print("Error - exercise without lesson found!")

        else:
            pass

    print(plan)
    command = input().split(":")