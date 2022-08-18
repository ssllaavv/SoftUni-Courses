activation_key = input()

while True:
    command = input().split(">>>")
    if command[0] == "Generate":
        break
    if command[0] == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        state = command[1]
        start_ind = int(command[2])
        end_ind = int(command[3])

        left_slice = activation_key[:start_ind]
        middle_slice = activation_key[start_ind: end_ind]
        right_slice = activation_key[end_ind:]

        if state == "Upper":
            activation_key = left_slice + middle_slice.upper() + right_slice
        elif state == "Lower":
            activation_key = left_slice + middle_slice.lower() + right_slice

        print(activation_key)

    elif command[0] == "Slice":
        start_ind = int(command[1])
        end_ind = int(command[2])

        left_slice = activation_key[:start_ind]
        right_slice = activation_key[end_ind:]
        activation_key = left_slice + right_slice

        print(activation_key)

print(f"Your activation key is: {activation_key}")
