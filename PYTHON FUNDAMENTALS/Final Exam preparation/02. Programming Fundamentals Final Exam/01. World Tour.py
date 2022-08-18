text = input()
text = text + " "

while True:
    input_line = input().split(":")
    command = input_line[0]
    if command == "Travel":
        break
    first_part = ""
    end_part = ""
    if command == "Add Stop":
        index = int(input_line[1])
        string = input_line[2]
        if index in range(len(text) - 1):
            first_part = text[: index]
            end_part = text[index:]
            text = first_part + string + end_part
        print(text)

    if command == "Remove Stop":
        start_index = int(input_line[1])
        end_index = int(input_line[2])
        if (start_index in range(len(text) - 1)) and (end_index in range(len(text))) and (start_index <= end_index + 1):
            first_part = text[: start_index]
            end_part = text[end_index + 1:]
            text = first_part + end_part
        print(text)

    if command == "Switch":
        old_string = input_line[1]
        new_string = input_line[2]
        if old_string in text:
            text = text.replace(old_string, new_string)
        print(text)

print(f"Ready for world tour! Planned stops: {text}")
