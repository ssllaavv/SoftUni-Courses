import re

inputs_count = int(input())
valid_pass_counter = 0
pattern = r"U\$(?P<user>[A-Z]{1}[a-z]{2,})U\$P@\$(?P<pass>[A-Za-z]{5,}\d+)P@\$"

for i in range(inputs_count):
    input_line = input()
    valid = re.findall(pattern, input_line)
    if valid:
        print("Registration was successful")
        print(f'Username: {valid[0][0]}, Password: {valid[0][1]}')
        valid_pass_counter += 1
    else:
        print("Invalid username or password")

print(f"Successful registrations: {valid_pass_counter}")