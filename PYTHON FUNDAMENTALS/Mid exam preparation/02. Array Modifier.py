def swap():
    list_of_ints[first_ind], list_of_ints[second_ind] = list_of_ints[second_ind], list_of_ints[first_ind]
    return list_of_ints

def multiply():
    list_of_ints[first_ind] = list_of_ints[first_ind] * list_of_ints[second_ind]
    return list_of_ints

def decrease():
    for i in range(len(list_of_ints)):
        list_of_ints[i] = list_of_ints[i] - 1
    return list_of_ints

list_of_ints = list(map(int, input().split()))
input_line = input()
while input_line != "end":
    command_llist = input_line.split()
    command = command_llist[0]
    if len(command_llist) > 1:
        first_ind = int(command_llist[1])
        second_ind = int(command_llist[2])
    if command == "swap":
        swap()
    elif command == "multiply":
        multiply()
    elif command == "decrease":
        decrease()
    input_line = input()
print(*list_of_ints, sep=", ")