# Task 1

message = input()

while True:
    command = input().split('|')
    if command[0] == 'Decode':
        break

    if command[0] == 'Move':
        count = int(command[1])
        message = message[count:] + message[: count]

    elif command[0] == 'Insert':
        index = int(command[1])
        value = command[2]
        message = message[: index] + value + message[index:]

    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        while substring in message:
            message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")


# Task 2
import re

text = input()
pattern = r'(?P<separator>[|#])(?P<item>[a-zA-Z]+(\s[a-zA-Z]+)*)' \
          r'(?P=separator)(?P<date>\d{2}/\d{2}/\d{2})' \
          r'(?P=separator)(?P<calories>0|([1-9][0-9]{0,3}|10000))(?P=separator)'

matches = [m.groupdict() for m in re.finditer(pattern, text)]

total_calories = 0
foods = {}

for match in matches:
    total_calories += int(match['calories'])
    foods[match['item']] = {'date': match['date'], 'calories': match['calories']}

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")
for food in foods.keys():
    print(f'Item: {food}, Best before: {foods[food]["date"]}, Nutrition: {foods[food]["calories"]}')



# Task 3

n = int(input())

pieces = {}

for _ in range(n):
    piece, composer, key = input().split('|')
    pieces[piece] = {'composer': composer, 'key': key}

while True:
    command = input().split('|')
    if command[0] == 'Stop':
        break

    if command[0] == 'Add':
        _, piece, composer, key = command
        if piece in pieces:
            print(f'{piece} is already in the collection!')
        else:
            pieces[piece] = {'composer': composer, 'key': key}
            print(f'{piece} by {composer} in {key} added to the collection!')

    elif command[0] == 'Remove':
        piece = command[1]
        if piece in pieces:
            del pieces[piece]
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif command[0] == 'ChangeKey':
        _, piece, new_key = command
        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

for piece in pieces.keys():
    print(f'{piece} -> Composer: {pieces[piece]["composer"]}, Key: {pieces[piece]["key"]}')





