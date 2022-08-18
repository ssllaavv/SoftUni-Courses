initial_list = input().split()

command = input().split()

while command != ['No', 'Money']:
    if command[0] == "OutOfStock":
        while command[1] in initial_list:
            index = initial_list.index(command[1])
            initial_list.pop(index)
            initial_list.insert(index, "None")

    if command[0] == "Required":
        if int(command[2]) < len(initial_list):
            initial_list.pop(int(command[2]))
            initial_list.insert(int(command[2]), (command[1]))

    if command[0] == "JustInCase":
        initial_list.pop()
        initial_list.append(command[1])
    command = input().split()

while "None" in initial_list:
    initial_list.remove("None")

print(*initial_list)
