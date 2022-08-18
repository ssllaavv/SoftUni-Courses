todo_list = [0] * 10

while True:
    command = list(input().split("-"))
    if command[0] == "End":
        break
    todo_list.pop(int(command[0]) - 1)
    todo_list.insert(int(command[0]) - 1, command[1])

todo_list = [element for element in todo_list if element != 0]

print(todo_list)


