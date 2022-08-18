raw_password = input()

while True:
    input_line = input().split()
    command = input_line[0]
    if command == "Done":
        break

    if command == "TakeOdd":
        raw_password = raw_password[1::2]
        print(raw_password)

    if command == "Cut":
        index = int(input_line[1])
        length = int(input_line[2])
        str_to_remove = raw_password[index:index + length]
        raw_password = raw_password.replace(str_to_remove, "", 1)
        print(raw_password)

    if command == "Substitute":
        substring = input_line[1]
        substitute = input_line[2]
        if substring in raw_password:
            raw_password = raw_password.replace(substring, substitute)
            print(raw_password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {raw_password}")

