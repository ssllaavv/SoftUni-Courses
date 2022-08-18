message = input()

while True:
    line_input = input().split(":|:")
    command = line_input[0]
    if command == "Reveal":
        break

    if command == "InsertSpace":
        index = int(line_input[1])
        first_part = message[:index]
        second_part = message[index:]
        message = first_part + " " + second_part
        print(message)

    if command == "Reverse":
        substring = ndex = line_input[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[:: -1]
            print(message)
        else:
            print("error")

    if command == "ChangeAll":
        substring = ndex = line_input[1]
        replacement = line_input[2]
        message = message.replace(substring, replacement)
        print(message)

print(f"You have a new text message: {message}")

