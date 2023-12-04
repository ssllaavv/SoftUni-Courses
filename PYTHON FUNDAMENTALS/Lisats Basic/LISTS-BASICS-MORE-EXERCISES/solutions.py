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

# read inputs (game state)
line_one = input().split()
line_two = input().split()
line_three = input().split()

# assign bool variables keep record if one of the players wins
first_wins = False
second_wins = False

# create matrix for game state
game = [line_one, line_two, line_three]

# check if any of the players satisfy the conditions to win the game
for c in range(3):
    if first_wins or second_wins:
        break
    if game[c][0] == game[c][1] == game[c][2] == "1":
        first_wins = True
    if game[c][0] == game[c][1] == game[c][2] == "2":
        second_wins = True
    if game[0][c] == game[1][c] == game[2][c] == "1":
        first_wins = True
    if game[0][c] == game[1][c] == game[2][c] == "2":
        second_wins = True
if game[0][0] == game[1][1] == game[2][2] == "1":
    first_wins = True
if game[0][2] == game[1][1] == game[2][0] == "1":
    first_wins = True
if game[0][0] == game[1][1] == game[2][2] == "2":
    second_wins = True
if game[0][2] == game[1][1] == game[2][0] == "2":
    second_wins = True

# print the result
if first_wins:
    print("First player won")
elif second_wins:
    print("Second player won")
else:
    print("Draw!")


# Task 6

# read inputs
numbers = list(map(int, input().split(' ')))

# read commands and process them until "end" command
while True:

    input_line = input()

    # break the cycle if end command is input
    if input_line == 'end':
        break

    token = input_line.split(' ')

    # handle exchange command
    if token[0] == 'exchange':
        index = int(token[1])

        if 0 <= index < len(numbers):
            numbers = numbers[index + 1:] + numbers[:index + 1]
        else:
            print("Invalid index")

    # in any other case except "end" and "exchange" command, there will be even/odd command
    # assign values to variable "odd_even_check" and use it in filter predicate
    else:
        odd_even_check = None
        if 'odd' in token:
            odd_even_check = 1
        elif 'even' in token:
            odd_even_check = 0

        # filter all odd/even elements
        filtered_numbers = [x for x in numbers if x % 2 == odd_even_check]

        # handle min/max command
        if token[0] in ['min', 'max']:

            if filtered_numbers:

                # the min/max input commands are same as min/max python functions - chan be patched directly into code
                num = eval(token[0])(filtered_numbers)
                # revere the list to find the last elements easier
                reversed_index = list(reversed(numbers)).index(num)
                index = len(numbers) - reversed_index - 1

                # print result
                print(index)

            else:
                print('No matches')

        # handel first/last commands
        elif token[0] in ['first', 'last']:
            count = int(token[1])

            if count > len(numbers):
                print("Invalid count")
            else:
                result = []
                if token[0] == 'last':
                    # reverse the list to find the last elements
                    filtered_numbers = list(reversed(filtered_numbers))
                    # reverse the result again to order in the elements as the original sequence
                    result = list(reversed(filtered_numbers[:count]))
                elif token[0] == 'first':
                    result = filtered_numbers[:count]

                # print the result
                print(result)

# print final state of the list
print(numbers)






