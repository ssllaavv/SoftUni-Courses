import os

# # Test 1

# try:
#     file = open('C:\\Users\\sslla\\Documents\\GitHub\\SoftUni-Courses\\PYTHON ADVANCED\\File Handling\\FILE-HANDLING-LAB\\text.txt' , 'r')
#     file.close()
# except FileNotFoundError:
#     print('File not found or path is incorrect')

# file = open('asd.txt', 'w')
# file.write('Hello, SoftUni!\nSecond line\nThird line')
# file.close()

# file = open('asd.txt')
# print(file.read(2))
# print(file.read(2))
# print(file.read(2))
# print(file.read())

# file = open('asd.txt')
# print(file.readline(5))
# print(file.readline(5))
# print(file.readline(5))
# print(file.readline())
# print(file.readline(5))
#

# file = open('asd.txt')
# lines = file.readlines()
# [print(line, end='') for line in lines]


# file = open('asd.txt')
# for line in file:
#     print(line, end='')
#
# try:
#     os.remove('text.txt')
# except FileNotFoundError:
#     print('File not found or path is incorrect')
# except PermissionError:
#     print('Close the file before deleting')
#
# # file = open('text.txt')
# # file.writelines('Hello')
# # file.writelines("This is my first file experiments")
# # file.readline()


# # Test 2
#
# file = open('text.txt')
# for line in file:
#     print(line, end='')
#
# # Teast 3
#
# file = open('python.txt', 'w')
# file.write(("This is the write command.\n"))
# file.write("It allows us to write in a particular file\n")
# file.close()
# file = open('python.txt', 'a')
# file.write('This is the third line.\n')
# file.write('And the forth line.\n')
# file = open('python.txt')
# for line in file:
#     print(line, end='')
#
# file.close()

# print(file.readline())
# print(file.readline())


# # Test 4

# file = open('python.txt', 'w')
#
# file.write('This is the write command.\n')
# file.write('It allow us to write in a particular file')
# file.close()
# file = open('python.txt')
# [print(line, end='') for line in file]
# file.close()
# os.remove('python.txt')


# Test 5

# file = open('python.txt', 'a')
# lines = ['line one\n', 'line two\n', 'line three\n']
# file.writelines(lines)
# file.close()
# file = open('python.txt', 'r')
# [print(line, end="") for line in file]
# file.close()
# os.remove('python.txt')


# # Test 6
#
# with open('text.txt', 'w') as f:
#     f.write('Hello world!!!')
#
# file_path = 'text.txt'
# if os.path.exists(file_path):
#     os.remove('text.txt')


# # Test 7

# with open('text.txt', 'w') as f:
#     f.write('Test file')
#
# try:
#     os.remove('text.txt')
# except FileNotFoundError:
#     print("File does not exist")


# Task 1

file = open('text.txt', 'w')
file.write('This is some random line\nThis is the second line\nAnd this is the third one')
file.close()

try:
    file = open('text.txt', 'r')
    print('File found')
    file.close()
except FileNotFoundError:
    print('File Not Found')

os.remove('text.txt')


# Task 2

file = open('numbers.txt', 'w')
file.write('1\n2\n3\n4\n5')
file.close()

file = open('numbers.txt')
sum_of_numbers = 0
for line in file:
    sum_of_numbers += int(line)

print(sum_of_numbers)
file.close()
os.remove('numbers.txt')

# Task 3

file = open('my_first_file.txt', 'w')
file.write("I've just created my first file!\nTheis is the second line.")
file.close()
file = open('my_first_file.txt', 'r')
print("".join(file.readlines()))
file.close()


# Task 4

try:
    os.remove('my_first_file.txt')
    print('Delete is successful')
except FileNotFoundError:
    print('File is already deleted')


# Task 5

import re

file = open('words.txt', 'w')
file.write('quick is fault')
file.close()

file = open('input.txt', 'w')
file.write(
    "-I was quick to judge him, but it wasn't his fault."
    "\n-Is this some kind of joke?! Is it?"
    "\n-Quick, hide here…It is safer."
)
file.close()

words_file = open('words.txt')
input_text_file = open('input.txt')

words = words_file.read().split(' ')
# print(words)


text = input_text_file.read()
pattern = r"\b[A-Za-z']+\b"
words_only = re.findall(pattern, text)
# print(words_only)
words_only_lower = []
for w in words_only:
    words_only_lower.append(w.lower())

words_dict = dict()
for w in words:
    words_dict[w] = 0

# print(words_dict)

for w in words_dict.keys():
    count = words_only_lower.count(w)
    words_dict[w] = count

sorted_words_dict = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words_dict:
    print(f"{word} - {count}")

words_file.close()
input_text_file.close()

os.remove('input.txt')
os.remove('words.txt')





