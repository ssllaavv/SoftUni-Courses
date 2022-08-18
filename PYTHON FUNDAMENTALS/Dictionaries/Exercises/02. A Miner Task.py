resources_dict = {}

while True:
    first_line = input()
    if first_line == "stop":
        break
    second_line = input()

    if first_line not in resources_dict:
        resources_dict[first_line] = 0
    resources_dict[first_line] += int(second_line)

for key, value in resources_dict.items():
    print(f"{key} -> {value}")
