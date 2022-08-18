gifts_list = input().split()

command = input()

while command != "No Money":
    command_list = command.split()
    if command_list[0] == "OutOfStock":
        for i in range(len(gifts_list)):
            if gifts_list[i] == command_list[1]:
                gifts_list[i] = "None"
    elif command_list[0] == "Required":
        if (int(command_list[2]) <= len(gifts_list) - 1) and int(command_list[2]) > 0:
            gifts_list.insert(int(command_list[2]), (command_list[1]))
            gifts_list.pop(int(command_list[2]) + 1)
    elif command_list[0] == "JustInCase":
        gifts_list.pop()
        gifts_list.append(command_list[1])
    command = input()

while "None" in gifts_list:
    gifts_list.remove("None")
print(*gifts_list)
