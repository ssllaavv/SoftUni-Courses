train_list = int(input()) * [0]

command = list(input().split())
while command[0] != "End":
    if command[0] == "add":
        train_list[-1] += int(command[1])
    elif command[0] == "insert":
        train_list[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        train_list[int(command[1])] -= int(command[2])
    command = list(input().split())

print(train_list)
