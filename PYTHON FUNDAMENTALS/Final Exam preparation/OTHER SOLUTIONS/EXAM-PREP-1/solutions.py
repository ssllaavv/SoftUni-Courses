# Task 1

password = input()

while True:
    command = input().split(' ')
    if command[0] == 'Done':
        break

    if command[0] == "TakeOdd":
        new_password = ""
        for i in range(1, len(password), 2):
            new_password += password[i]
        password = new_password
        print(password)

    elif command[0] == "Cut":
        index, length = int(command[1]), int(command[2])
        substring = password[index: index + length]
        password = password.replace(substring, "")
        print(password)

    elif command[0] == "Substitute":
        substring, substitute = command[1], command[2]
        if substring in password:
            while substring in password:
                password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f'Your password is: {password}')


# Task 2
import re

text = input()

pattern_numbers = r'\d'
pattern_emojis = r'(\*{2}|:{2})(?P<emojy>[A-Z][a-z]{2}[a-z]*)(\1)'

numbers = re.findall(pattern_numbers, text)

threshold = 1
for n in numbers:
    threshold *= int(n)

emojis = [m.group() for m in re.finditer(pattern_emojis, text)]

# print(emojis)

emojis_dict = {e: sum([ord(l) for l in e[2: -2]]) for e in emojis}

print(f'Cool threshold: {threshold}\n'
      f'{len(emojis)} emojis found in the text. '
      f'The cool ones are:')

for emojy, value in emojis_dict.items():
    if value >= threshold:
        print(emojy)


# Task 3

planets = {}

n = int(input())
for _ in range(n):
    planet, rarity = input().split('<->')
    planets[planet] = {'rarity': int(rarity), 'ratings': []}

while True:
    command_line = input().split(': ')
    if command_line[0] == "Exhibition":
        break

    command, arguments = command_line

    if command == 'Reset':
        planet = arguments
        if planet not in planets:
            print('error')
            continue
        planets[planet]['ratings'] = []

    else:
        planet, value = arguments.split(' - ')
        if planet not in planets:
            print('error')
            continue

        if command == 'Rate':
            planets[planet]['ratings'].append(int(value))

        elif command == 'Update':
            planets[planet]['rarity'] = int(value)

print("Plants for the exhibition:")
for p, v in planets.items():

    rating = 0
    if v['ratings']:
        rating = sum(v['ratings']) / len(v['ratings'])

    print(f'- {p}; Rarity: {v["rarity"]}; Rating: {rating:.2f}')




























