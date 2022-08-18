input_text = input()

while True:
    input_line = input().split(" ")
    command = input_line[0]

    if command == "Easter":
        break

    if command == "Replace":
        current_char = input_line[1]
        new_char = input_line[2]
        input_text = input_text.replace(current_char, new_char)
        print(input_text)

    if command == "Remove":
        substring = input_line[1]
        input_text = input_text.replace(substring, "")
        print(input_text)

    if command == "Includes":
        string = input_line[1]
        print(string in input_text)

    if command == "Change":
        sub_command = input_line[1]
        if sub_command == "Upper":
            input_text = input_text.upper()
        if sub_command == "Lower":
            input_text = input_text.lower()
        print(input_text)

    if command == "Reverse":
        start_index = int(input_line[1])
        end_index = int(input_line[2])
        if (start_index in range(len(input_text))) and (end_index in range(len(input_text) + 1)):
            if end_index > start_index:
                new_string = input_text[start_index: end_index + 1]
                reversed_string = new_string[:: -1]
                print(reversed_string)