import os

# Task 1

with open('text.txt', 'w') as f:
    f.write(
        "-I was quick to judge him, but it wasn't his fault."
        "\n-Is this some kind of joke?! Is it?"
        "\n-Quick, hide here. It is safer."
    )

with open('text.txt', 'r') as file:
    lines = file.readlines()
    output = []
    for i in range(len(lines)):
        if i % 2 == 0:
            line = lines[i]
            modified_line = line
            for l in line:
                if l in ["-", ",", ".", "!", "?"]:
                    modified_line = modified_line.replace(l, '@')
                if l == '\n':
                    modified_line = modified_line.replace(l, '')
            reversed_line = " ".join(list(reversed(modified_line.split(' '))))
            output.append(reversed_line)

    print("\n".join(output))
os.remove('text.txt')


# Task 2

input_file = open('text.txt', 'w')
input_file.write(
    "-I was quick to judge him, but it wasn't his fault."
    "\n-Is this some kind of joke?! Is it?"
    "\n-Quick, hide here. It is safer."
    )
input_file.close()
input_file = open('text.txt', 'r')

output_file = open('output.txt', 'w')
lines = input_file.readlines()
for i in range(len(lines)):
    line = lines[i].replace('\n', '')
    letters = 0
    punctuations = 0
    for l in lines[i]:
        if l.isalnum():
            letters += 1
        elif l in ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']:
            punctuations += 1

    output_file.writelines(f"Line {i + 1} {line} ({letters})({punctuations})\n")
output_file.close()

output_file = open('output.txt')

print(output_file.read())

output_file.close()
input_file.close()

os.remove('output.txt')
os.remove('text.txt')


# Task 3

while True:
    command_token = input()

    if command_token == "End":
        break

    else:
        command = command_token.split("-")

        if command[0] == "Create":
            file_name = command[1]
            with open(file_name, 'w') as f:
                ...

        elif command[0] == "Add":
            file_name = command[1]
            content = command[2]
            with open(file_name, 'a') as f:
                f.write(f"{content}\n")

        elif command[0] == "Replace":
            file_name = command[1]
            old_string = command[2]
            new_string = command[3]
            try:
                with open(file_name, 'r') as f:
                    old_text = f.read()
                with open(file_name, 'w') as f:
                    new_text = old_text.replace(old_string, new_string)
                    f.write(new_text)
            except FileNotFoundError:
                print("An error occurred")

        elif command[0] == "Delete":
            file_name = command[1]
            try:
                os.remove(file_name)
            except FileNotFoundError:
                print("An error occurred")


# Task 4

directory_path = 'C:\\Users\\sslla\\Desktop\\SOFTUNI\\DEVOPS\\CONTAINERS AND CLOUD\\6. Exercise Containers and Docker\solutions\\fiFirst try\\07.Tracker-App'
content = os.listdir(directory_path)
files_only = []

for item in content:
    item_path = os.path.join(directory_path, item)
    if os.path.isfile(item_path):
        files_only.append(item)

files_and_extensions = [item.split(".") for item in files_only]

# print(files_and_extensions)

full_file_names_and_extensions = [[".".join(item[:-1]), item[-1]] if len(item) > 1 else [item[0], ''] for item in files_and_extensions]

# print(full_file_names_and_extensions)

files_dict = {}
for file in full_file_names_and_extensions:
    if file[1] not in files_dict.keys():
        files_dict[file[1]] = []
    files_dict[file[1]].append(file[0])

sorted_files_dict = dict(sorted(files_dict.items()))

# print(sorted_files_dict)

for extension, files in sorted_files_dict.items():
    print(f".{extension}")
    for file in sorted(files):
        print(f"- - - {file}.{extension}")










