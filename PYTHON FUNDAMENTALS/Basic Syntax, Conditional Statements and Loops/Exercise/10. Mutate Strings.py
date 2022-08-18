first_string = input()
second_string = input()

previous_string = first_string
for i in range(len(first_string)):
    end = first_string[i + 1:]
    start = second_string[:i + 1]
    current_string = start + end

    if previous_string == current_string:
        continue
    else:
        print(current_string)
    previous_string = current_string
