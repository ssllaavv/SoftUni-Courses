
# Task 1

usernames = input().split(', ')

valid_usernames = []

for username in usernames:
    is_valid = True

    for l in username:
        if not (l.isalnum() or l in ['_', '-']):
            is_valid = False
    if not 3 <= len(username) <= 16:
        is_valid = False

    if is_valid:
        valid_usernames.append(username)

print('\n'.join(valid_usernames))


# Task 2

word_1, word_2 = input().split(' ')

min_len = min(len(word_1), len(word_2))

result = 0

for i in range(min_len):
    result += ord(word_1[i]) * ord(word_2[i])

for l in word_1[min_len:]:
    result += ord(l)

for l in word_2[min_len:]:
    result += ord(l)

print(result)



# Task 3

file_path = input().split('\\')

file_name, extension = file_path[-1].split('.')

print(f'File name: {file_name}')
print(f'File extension: {extension}')


# Task 4

text = input()
encrypted_text = ""

for l in text:
    encrypted_text += chr(ord(l) + 3)

print(encrypted_text)


# Task 5

text = input()
emoticons = []

for i in range(len(text)):
    if text[i] == ':':
        if text[i + 1] != " ":
            emoticons.append(text[i] + text[i + 1])

print('\n'.join(emoticons))


# Task 6

text = input()
result = ''

i = 0
while True:
    if i >= len(text):
        break

    result += text[i]
    while i < len(text) - 1 and text[i] == text[i + 1]:
        i += 1
    i += 1

print(result)


# Task 7

text = input()

strength = 0
result = ""

for index in range(len(text)):
    if strength == 0:
        if text[index] != ">":
            result += text[index]
        else:
            strength = int(text[index + 1])
            result += ">"
    else:
        if text[index] != ">":
            strength -= 1
            continue
        else:
            strength += int(text[index + 1])
            result += ">"

print(result)


# Task 8

total_sum = 0
input_line = input().split()


for el in input_line:

    first_letter = el[0]
    last_letter = el[-1]
    number = int(el[1: - 1])

    if first_letter.islower():
        number *= ord(first_letter) - 96
    else:
        number /= ord(first_letter) - 64

    if last_letter.islower():
        number += ord(last_letter) - 96
    else:
        number -= ord(last_letter) - 64

    total_sum += number

print(f'{total_sum:.2f}')


# Task 9

text = input()

unique_symbols = []
text_dict = {}

word = ''
count = 0
i = 0

while i <= len(text) - 1:
    if not text[i].isdigit():
        word += text[i].upper()
        if text[i].upper() not in unique_symbols:
            unique_symbols.append(text[i].upper())
        i += 1
    else:
        if i < len(text) - 1 and text[i + 1].isdigit():
            count = int(text[i: i + 2])
            i += 1
        else:
            count = int(text[i])

        i += 1
        text_dict[word] = count
        count = 0
        word = ''

result = ''
for k, v in text_dict.items():
    result += k * v

print(f'Unique symbols used: {len(unique_symbols)}')
print(result)



# Task 10

tickets = input().split(', ')

for t in tickets:
    t = t.strip()
    if len(t) != 20:
        print("invalid ticket")
    else:
        left_part = t[0: 10]
        right_part = t[10:]

        no_match = True
        for s in ['@', '#', '$', '^']:
            if s * 10 in left_part and s * 10 in right_part:
                print(f'ticket "{t}" - 10{s} Jackpot!')
                no_match = False
            else:
                for count in range(9, 5, -1):
                    if s * count in left_part and s * count in right_part:
                        print(f'ticket "{t}" - {count}{s}')
                        no_match = False
                        break

        if no_match:
            print(f'ticket "{t}" - no match')





















