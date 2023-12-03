# Task 1 - solution 1

# read the input
numbers = list(map(int, input().split(', ')))

counter = 0

# remove all zeroes
while 0 in numbers:
    numbers.remove(0)
    counter += 1

# add the zeroes at the end of the list
numbers += [0] * counter

# print the result
print(numbers)


# Task 1 - solution 2

# read the input
numbers = list(map(int, input().split(', ')))

zeroes = []

# pop all zeroes and add then in a separate list
while 0 in numbers:
    index = numbers.index(0)
    zeroes.append(numbers.pop(index))

#  extend the numbers list with zeroes list
numbers.extend(zeroes)

print(numbers)


# Task 1  - solution 3

# read the input
numbers = list(map(int, input().split(', ')))

# find count od zeroes
z_count = numbers.count(0)

# filter numbers list
filtered_numbers = list(filter(lambda x: x != 0, numbers))

# add zeroes at the end of the filtered list
filtered_numbers += [0] * z_count

# print the result
print(filtered_numbers)


# Task 2 - solution 1

# read the inputs
numbers = input().split(' ')
text = list(input())

# declare output variable
message = ""

# calculate valid indexes, pop the string for the text list and add it to message
for number in numbers:
    digits = list(map(int, number))
    index = sum(digits) % len(text)
    message += str(text.pop(index))

# print the result message
print(message)


# Task 2 - solution 2

# read the inputs
numbers = list(map(int, input().split(' ')))
text = list(input())

# declare output variable
message = ""

# calculate valid indexes, pop the string for the text list and add it to message
for number in numbers:
    index = 0
    while number > 0:
        index += number % 10
        number //= 10
    message += str(text.pop(index % len(text)))

# print the result message
print(message)


# Task 3

# read the input
times = list(map(int, input().split(' ')))

# find the middle index element
middle_index = len(times) // 2 + 1

# create separate lists for each player
left_times = times[:middle_index - 1]
right_times = times[middle_index:]

left_time = 0
right_time = 0

# calculate left time
for t in left_times:
    if t == 0:
        left_time *= .8
    else:
        left_time += t

# calculate right time
for t in reversed(right_times):
    if t == 0:
        right_time *= .8
    else:
        right_time += t

# assign winner and winners time
if left_time < right_time:
    winner = 'left'
    time = left_time
else:
    winner = 'right'
    time = right_time

# print the result
print(f'The winner is {winner} with total time: {time:.1f}')


# Task 4

# read the input
people = list(map(int, input().split(' ')))
k = int(input())

# assign variable for the result
ordered_people = []

# assign reminder to keep track of the current state of circle start point
remainder = 0

# start counting and removing people until noone left
while people:
    index = (k + remainder) % len(people)
    ordered_people.append(people.pop(index - 1))
    remainder = index - 1
    if remainder < 0:
        remainder = len(people) - remainder - 1

# print the result
print(f'[{",".join(list(map(str, ordered_people)))}]')


# Task 5

# read the input
first_line = input().split(' ')
second_line = input().split(' ')
third_line = input().split(' ')

# create matrix
matrix = [first_line, second_line, third_line]

# assign booleans for game results
first_wins = False
second_wins = False

# check horizontals
for line in matrix:
    if all(x == '1' for x in line):
        first_wins = True
    elif all(x == '2' for x in line):
        second_wins = True

# check verticals
for r in range(3):
    column = []
    for c in range(3):
        column.append(matrix[r][c])

    if all(x == '1' for x in column):
        first_wins = True
    elif all(x == '2' for x in column):
        second_wins = True

# read diagonals state
left_diagonal = [matrix[0][0], matrix[1][1], matrix[2][2]]
right_diagonal = [matrix[0][2], matrix[1][1], matrix[2][0]]


# check diagonals
if all(x == '1' for x in left_diagonal) \
        or all(x == '1' for x in right_diagonal):
    first_wins = True
elif all(x == '2' for x in left_diagonal) \
        or all(x == '2' for x in right_diagonal):
    second_wins = True

# print result
if first_wins and second_wins or not first_wins and not second_wins:
    print("Draw!")
elif first_wins:
    print('First player won')
elif second_wins:
    print('Second player won')


# Task 6

# read inputs
numbers = list(map(int, input().split(' ')))

while True:

    input_line = input()
    if input_line == 'end':
        break

    token = input_line.split(' ')

    if token[0] == 'exchange':
        index = int(token[1])

        if 0 <= index < len(numbers):
            numbers = numbers[index + 1:] + numbers[:index + 1]
        else:
            print("Invalid index")

    else:
        check = None
        if 'odd' in token:
            check = 1
        elif 'even' in token:
            check = 0
        filtered_numbers = [x for x in numbers if x % 2 == check]

        if token[0] in ['min', 'max']:

            if filtered_numbers:
                max_num = eval(token[0])(filtered_numbers)
                reversed_index = list(reversed(numbers)).index(max_num)
                index = len(numbers) - reversed_index - 1

                print(index)

            else:
                print('No matches')

        elif token[0] in ['first', 'last']:
            count = int(token[1])

            if count > len(numbers):
                print("Invalid count")
            else:
                result = []
                if token[0] == 'last':
                    filtered_numbers = list(reversed(filtered_numbers))
                    result = list(reversed(filtered_numbers))[:count]
                elif token[0] == 'first':
                    result = filtered_numbers[:count]

                print(result)

print(numbers)






