input_line = input()
chars_dict = {}

for char in input_line:
    if (char not in chars_dict) and (char != " "):
        chars_dict[char] = 0
    if (char in chars_dict) and (char != " "):
        chars_dict[char] += 1

for key, value in chars_dict.items():
    print(f"{key} -> {value}")


