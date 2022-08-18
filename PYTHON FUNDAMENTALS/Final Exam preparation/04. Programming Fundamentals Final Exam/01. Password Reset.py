raw_password = input()

password_as_list = []
new_password_as_list = []

line_input = input().split(" ")
while line_input[0] != "Done":
    command = line_input[0]
    if command == "TakeOdd":
        for el in raw_password:
            password_as_list.append(el)

        for i in range(1, len(password_as_list), 2):
            new_password_as_list += password_as_list[i]
        raw_password = ""
        for el in new_password_as_list:
            raw_password += el
        print(raw_password)

    if command == "Cut":
        start_index = int(line_input[1])
        end_index = int(line_input[1]) + int(line_input[2])

        first_part = raw_password[:start_index]
        second_part = raw_password[start_index: end_index]
        third_part = raw_password[end_index:]

        raw_password = first_part + third_part
        print(raw_password)

    if command == "Substitute":
        substring = line_input[1]
        substitute = line_input[2]

        if substring in raw_password:
            raw_password = raw_password.replace(substring, substitute)
            print(raw_password)
        else:
            print("Nothing to replace!")

    line_input = input().split(" ")
print(f"Your password is: {raw_password}")
