# Task 1

key = input()

while True:
    command = input().split('>>>')
    if command[0] == 'Generate':
        break

    if command[0] == 'Contains':
        substring = command[1]
        if substring in key:
            print(f'{key} contains {substring}')
        else:
            print(f'Substring not found!')

    elif command[0] == 'Flip':
        subcommand = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        string_to_convert = key[start_index: end_index]

        if subcommand == 'Upper':
            string_to_convert = string_to_convert.upper()

        elif subcommand == "Lower":
            string_to_convert = string_to_convert.lower()

        key = key[: start_index] + string_to_convert + key[end_index:]
        print(key)

    elif command[0] == 'Slice':
        start_index = int(command[1])
        end_index = int(command[2])
        key = key[: start_index] + key[end_index:]
        print(key)

print(f'Your activation key is: {key}')


# Task 2
import re
n = int(input())

pattern_validate = r'^@#+(?P<barcode>[A-Z][a-zA-Z\d]{4}[a-zA-Z\d]*[A-Z])(@#+)$'
pattern_prod_group = r'\d'

for _ in range(n):
    barcode = input()
    match = re.search(pattern_validate, barcode)
    if match:
        barcode_filtered = match.groupdict()['barcode']
        matches = re.findall(pattern_prod_group, barcode_filtered)
        prod_group = ''.join(matches)
        if prod_group:
            print(f'Product group: {prod_group}')
        else:
            print('Product group: 00')

    else:
        print('Invalid barcode')


# Task 3

n = int(input())

cars = {}

for _ in range(n):
    car, mileage, fuel = input().split('|')
    cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

while True:
    command_line = input().split(' : ')
    if command_line[0] == 'Stop':
        break

    if command_line[0] == 'Drive':
        _, car, distance, fuel = command_line
        if int(fuel) > cars[car]['fuel']:
            print('Not enough fuel to make that ride')
        else:
            cars[car]['mileage'] += int(distance)
            cars[car]['fuel'] -= int(fuel)
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
            if cars[car]['mileage'] >= 100_000:
                del cars[car]
                print(f'Time to sell the {car}!')

    elif command_line[0] == 'Refuel':
        _, car, fuel = command_line
        if cars[car]['fuel'] + int(fuel) > 75:
            fuel = 75 - cars[car]['fuel']
            cars[car]['fuel'] = 75
        else:
            cars[car]['fuel'] += int(fuel)
        print(f'{car} refueled with {fuel} liters')

    elif command_line[0] == 'Revert':
        _, car, kilometers = command_line
        if cars[car]['mileage'] - int(kilometers) < 10_000:
            cars[car]['mileage'] = 10_000
        else:
            cars[car]['mileage'] -= int(kilometers)
            print(f'{car} mileage decreased by {kilometers} kilometers')

for car in cars.keys():
    print(f'{car} -> Mileage: {cars[car]["mileage"]} kms, Fuel in the tank: {cars[car]["fuel"]} lt.')






































