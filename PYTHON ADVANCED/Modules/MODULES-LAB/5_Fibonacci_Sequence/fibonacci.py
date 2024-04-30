def fibonacci_game():

    fibonacci_list = []

    while True:
        command = input()
        if command == "Stop":
            break
        command_token = command.split()
        if command_token[0] == "Create":
            length = int(command_token[2])
            if length == 1:
                fibonacci_list = [0, ]
            elif length == 2:
                fibonacci_list = [0, 1]
            else:
                fibonacci_list = [0, 1]
                for _ in range(length - 2):
                    fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

            print(*fibonacci_list)

        elif command_token[0] == "Locate":
            num = int(command_token[1])

            try:
                index = fibonacci_list.index(num)
                print(f"The number - {num} is at index {index}")
            except(ValueError):
                print(f"The number {num} is not in the sequence")

