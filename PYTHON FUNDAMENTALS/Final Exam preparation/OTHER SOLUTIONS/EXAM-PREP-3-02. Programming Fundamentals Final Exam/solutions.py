# Task 1
text = input()

while True:
    command = input().split(':')
    if command[0] == 'Travel':
        break

    if command[0] == 'Add Stop':
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(text):
            text = text[:index] + string + text[index:]
        print(text)

    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(text) and 0 <= end_index < len(text):
            text = text[: start_index] + text[end_index + 1:]
        print(text)

    elif command[0] == 'Switch':
        _, old_string, new_string = command
        text = text.replace(old_string, new_string)
        print(text)

print(f'Ready for world tour! Planned stops: {text}')


# Task 2
import re

text = input()
destinations = []
points = 0
pattern = r'(?P<separator>[=/])(?P<destination>[A-Z][a-zA-Z]{2,})(?P=separator)'

matches = [m.groupdict() for m in re.finditer(pattern, text)]

for match in matches:
    destinations.append(match['destination'])
    points += len(match['destination'])

print(f'Destinations: {", ".join(destinations)}')
print(f'Travel Points: {points}')


# Task 3

n = int(input())
plants = {}

for _ in range(n):
    plant, rarity = input().split('<->')
    plants[plant] = {'rarity': int(rarity), 'ratings': []}

while True:
    command_line = input().split(': ')
    if command_line[0] == 'Exhibition':
        break

    command, subcommand = command_line
    subcommand = subcommand.split(' - ')
    plant = subcommand[0]

    if plant not in plants:
        print('error')

    else:

        if command == 'Rate':
            _, rating = subcommand
            plants[plant]['ratings'].append(int(rating))

        elif command == 'Update':
            _, rarity = subcommand
            plants[plant]['rarity'] = int(rarity)

        elif command == 'Reset':
            plants[plant]['ratings'] = []

print('Plants for the exhibition:')
for p in plants.keys():
    avg_rating = 0
    if plants[p]['ratings']:
        avg_rating = sum(plants[p]['ratings']) / len(plants[p]['ratings'])
    print(f'- {p}; Rarity: {plants[p]["rarity"]}; Rating: {avg_rating:.2f}')
























