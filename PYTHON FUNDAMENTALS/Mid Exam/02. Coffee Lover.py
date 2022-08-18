list_of_coffees = input().split()
commands_count = int(input())

for n in range(1, commands_count + 1):
    command = input().split()
    if command[0] == "Include":
        list_of_coffees.append(command[1])

    elif command[0] == "Remove":
        number_of_coffees = int(command[2])
        if number_of_coffees > len(list_of_coffees):
            continue
        if command[1] == "last":
            for _ in range(number_of_coffees):
                list_of_coffees.pop()
        elif command[1] == "first":
            for _ in range(number_of_coffees):
                list_of_coffees.pop(0)

    elif command[0] == "Prefer":
        first_index = int(command[1])
        second_index = int(command[2])
        if first_index not in range(len(list_of_coffees)) and\
                second_index not in range(len(list_of_coffees)):
            continue
        list_of_coffees[first_index], list_of_coffees[second_index] = \
            list_of_coffees[second_index], list_of_coffees[first_index]

    elif command[0] == "Reverse":
        list_of_coffees = reversed(list_of_coffees)

print("Coffees:")
print(*list_of_coffees)
