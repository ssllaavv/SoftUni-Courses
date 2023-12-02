# Task 1 - solution 1

print(list(map(lambda x: -x,  (map(int, input().split(' '))))))

# Task 1 - solution 2

numbers = list(map(int, input().split(' ')))

opposite_numbers = list(map(lambda x: -x, numbers))

print(opposite_numbers)


# Task 1 -solution 3

numbers = list(map(int, input().split(' ')))

opposite_numbers = []
for n in numbers:
    opposite_numbers.append(-1 * n)

print(opposite_numbers)


# Task 2 - solution 1

factor = int(input())
count = int(input())

numbers = list()

for n in range(1, count + 1):
    numbers.append(factor * n)

print(numbers)


# Task 2 - solution 2

factor = int(input())
count = int(input())

numbers = [n * factor for n in range(1, count + 1)]

print(numbers)


# Task 3
team_a = [i for i in range(1, 12)]
team_b = [i for i in range(1, 12)]

commands = input().split(' ')

while len(team_a) > 6 and len(team_b) > 6 and commands:

    team, player = commands.pop(0).split('-')

    if team == 'A' and int(player) in team_a:
        team_a.remove(int(player))
    elif team == 'B' and int(player) in team_b:
        team_b.remove(int(player))

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if len(team_a) == 6 or len(team_b) == 6:
    print('Game was terminated')


# Task 4
numbers = list(map(int, input().split(', ')))
beggars_count = int(input())

beggars_list = [0] * beggars_count

while numbers:
    for i in range(len(beggars_list)):
        if numbers:
            beggars_list[i] += numbers.pop(0)

print(beggars_list)


# Task 5

deck = input().split(' ')
count = int(input())

result_deck = []

for i in range(count):

    bottom_half = deck[: len(deck) // 2]
    top_half = deck[len(deck) // 2:]

    while bottom_half or top_half:
        if bottom_half:
            result_deck.append(bottom_half.pop(0))
        if top_half:
            result_deck.append(top_half.pop(0))

    deck = result_deck.copy()
    result_deck.clear()

print(deck)


# Task 6 - solution 1

numbers = list(map(int, input().split(' ')))
count = int(input())

for i in range(count):
    smallest_number = numbers[0]

    for n in numbers:
        if n < smallest_number:
            smallest_number = n

    numbers.remove(smallest_number)

print(numbers[0], end="")
for n in range(1, len(numbers)):
    print(f", {numbers[n]}", end='')


# Task 6 - solution 2

numbers = list(map(int, input().split(' ')))
count = int(input())

for i in range(count):
    numbers.remove(min(numbers))

print(', '.join(list(map(str, numbers))))


# Task 7

gifts = input().split(' ')

while True:
    command_line = input()

    if command_line == 'No Money':
        break

    command_line_list = command_line.split(' ')
    command = command_line_list.pop(0)

    if command == 'OutOfStock':
        gift = command_line_list[0]
        gift_indexes = [ind for ind, value in enumerate(gifts) if value == gift]
        for i in gift_indexes:
            gifts[i] = None

    elif command == 'Required':
        gift = command_line_list[0]
        gift_index = int(command_line_list[1])
        if 0 <= gift_index < len(gifts):
            gifts[gift_index] = gift

    elif command == 'JustInCase':
        gift = command_line_list[0]
        gifts[-1] = gift

filtered_gifts = [g for g in gifts if g]

print(' '.join(filtered_gifts))


# Task 8

# read inputs

fires_token = input().split('#')
water = int(input())

# # convert input line in list of tuples by list comprehension

# fires = [(level, int(value)) for level, value in [token.split(" = ") for token in fires_token]]

# alternatively, use for cycles:

fires = []
for el in fires_token:
    fire = el.split(' = ')
    fires.append(tuple([fire[0], int(fire[1])]))

# assign temp variables

cells_extinguished = []

# extinguish fires
while fires and water:

    min_level_of_fires = min([value for _, value in fires]) or 0
    if water < min_level_of_fires:
        break

    i = 0
    while i < len(fires):

        level, value = fires[i]

        if level == 'Low' and 0 < value < 51 \
                or level == 'Medium' and 50 < value < 81 \
                or level == 'High' and 80 < value < 126:

            if water >= value:
                water -= value
                cells_extinguished.append(value)
                fires.remove(fires[i])
            else:
                i += 1

        else:
            fires.remove(fires[i])


total_fire = sum(cells_extinguished)
total_effort = total_fire / 4

print('Cells:')
for value in cells_extinguished:
    print(f'- {value}')

print(f'Effort: {total_effort:.2f}\nTotal Fire: {total_fire}')


# Task 9

# read inputs
items_tokenS = input().split('|')
budget = int(input())

# declare variables
sold_products_prices = []
items = []

# parse items to list of tuples
for el in items_tokenS:
    item, price = el.split('->')
    items.append((item, float(price)))

# buy and sell items, add them to sold list
for item, price in items:
    if budget > 0:
        if item == 'Clothes' and price <= 50 or \
                item == 'Shoes' and price <= 35 or \
                item == 'Accessories' and price <= 20.50:
            if budget >= price:
                budget -= price
                sold_products_prices.append(price * 1.4)

# calculate profit and budget
total_income = sum(sold_products_prices)
profit = total_income - total_income / 1.4
budget += total_income

# print the output
for el in sold_products_prices:
    print(f'{el:.2f}', end=' ')

print(f'\nProfit: {profit:.2f}')
print('Hello, France!' if budget > 150 else 'Not enough money.')


# Task 10

# read the input
command_tokens = input().split('|')

# define variables
energy = 100
coins = 100
is_bankrupted = False

# start the restaurant business
for token in command_tokens:
    command = token.split('-')[0]
    value = int(token.split('-')[1])

    # handle 'rest' case
    if command == 'rest':
        if energy + value > 100:
            value = 100 - energy
            energy = 100
        else:
            energy += value
        print(f'You gained {value} energy.\n'
              f'Current energy: {energy}.')

    # handle 'orders'
    elif command == 'order':
        if energy >= 30:
            energy -= 30
            coins += value
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print('You had to rest!')

    # handle ingredients buying
    else:
        if value <= coins:
            coins -= value
            print(f'You bought {command}.')
        else:
            print(f'Closed! Cannot afford {command}.')
            is_bankrupted = True
            break

# print output
if not is_bankrupted:
    print(f'Day completed!\n'
          f'Coins: {coins}\n'
          f'Energy: {energy}')
