# Task 1
def find_diagonals():
    size = int(input())
    matrix = [[int(x) for x in input().split(', ')] for _ in range(size)]

    primary_diagonal = [matrix[i][i] for i in range(size)]
    secondary_diagonal = list(reversed([matrix[i][size - 1 - i] for i in range(size - 1, -1, -1)]))

    return [primary_diagonal, secondary_diagonal]


# primary_diagonal, secondary_diagonal = find_diagonals()
# print(f'Primary diagonal: {", ".join(list(map(str, primary_diagonal)))}. '
#              f'Sum: {sum(primary_diagonal)}')
# print(f'Secondary diagonal: {", ".join(list(map(str, secondary_diagonal)))}. '
#              f'Sum: {sum(secondary_diagonal)}')


# Task 2
def find_diagonals():
    size = int(input())
    matrix = [[int(x) for x in input().split(' ')] for _ in range(size)]

    primary_diagonal = [matrix[i][i] for i in range(size)]
    secondary_diagonal = list(reversed([matrix[i][size - 1 - i] for i in range(size - 1, -1, -1)]))

    return [primary_diagonal, secondary_diagonal]


primary, secondary = find_diagonals()
# print(primary)
# print(secondary)
# print(sum(primary))
# print(sum(secondary))
# print(sum(primary) - sum(secondary))
print(abs(sum(primary) - sum(secondary)))


# Task 3

rows, cols = [int(x)for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]
count = 0
for r in range(rows - 1):
    for c in range(cols - 1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            count += 1
print(count)


# Task 4
from sys import maxsize

rows, cols = [int(x) for x in input().split()]
if rows >= 3 and cols >= 3:  # The problem make sense only if side ot initial matrix is larger , than 3x3
    matrix = [[int(x) for x in input().split()] for _ in range(rows)]
    x, y = [None, None]  # start indexes fo max_sum_square 3x3
    max_sum = -maxsize

    # iterate through all possible start indexes of 3x3 squares  -> (size - 2) not inclusive:
    for r in range(rows - 2):
        for c in range(cols - 2):
            current_sum = 0
            # calculate sum of the 3X3 square:
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    current_sum += matrix[i][j]
            if current_sum > max_sum:
                max_sum = current_sum
                x, y = [r, c]  # keep the starting coordinates if max square 3x3

    print(f'Sum = {max_sum}')
    for r in range(x, x + 3):
        print(" ".join([str(n) for n in matrix[r][y: y + 3]]))  # print max 3x3 sub-matrix


# Task 5

rows, cols = [int(x) for x in input().split()]
matrix = []
a = 97

for r in range(rows):
    matrix.append([])
    for c in range(cols):
        matrix[r].append(chr(a + r) + chr(a + r + c) + chr(a + r))

for r in matrix:
    print(' '.join(r))


# Task 6

rows, cols = [int(x) for x in input().split()]      # read the size of the matrix
matrix = [input().split() for _ in range(rows)]     # read the matrix

while True:     # start reading command until 'END' command
    command = input().split()
    if command[0] == 'END':
        break

        # check if the input is valid :
    if command[0] != 'swap' or \
            len(command) != 5 or \
            not all(x.isdigit() for x in command[1:]) or \
            not all([(0 <= int(command[y]) < rows) for y in range(1, 5, 2)]) or \
            not all([(0 <= int(command[y]) < cols) for y in range(2, 5, 2)]):
        print('Invalid input!')

    else:   # swap the places of the elements in the specified indexes
        matrix[int(command[1])][int(command[2])], matrix[int(command[3])][int(command[4])] = \
            matrix[int(command[3])][int(command[4])], matrix[int(command[1])][int(command[2])]
        for r in matrix:    # print the matrix
            print(' '.join(list(map(str, r))))



# Task 7

from collections import deque

rows, cols = [int(x) for x in input().split()]
text = deque(input())
matrix = []

for r in range(rows):
    matrix.append([])
    for c in range(cols):
        letter = text.popleft()
        text.append(letter)
        if r % 2 == 0:
            matrix[r].append(letter)
        else:
            matrix[r].insert(0, letter)

for r in matrix:
    print(''.join(r))



# Task 8

size = int(input())  # read the size of the square matrix
matrix = [list(map(int, input().split())) for _ in range(size)]  # read the matrix

bombs_token = input().split(' ')  # read the bombs input
bombs = [[int(x) for x in el.split(',')] for el in bombs_token]  # transform bombs input ito 2d coordinates

for bomb in bombs:   # start to detonate the bombs
    r, c = bomb   # translate bomb coordinate to rol and column
    value = matrix[r][c]  # get the value of the explosion
    if value > 0:  # check if the bomb is not yet utilized
        for i in range(max((r - 1), 0), min((r + 2), size)):  # iterate a row above and below the bomb coordinate
            for j in range(max((c - 1), 0), min((c + 2), size)): # iterate a column before and after the bomb coordinate
                if matrix[i][j] > 0:  # check if the cell is alive
                    matrix[i][j] -= value  # if alive, try killing it !
        matrix[r][c] = 0  # mark the bomb as detonated

alive_count = 0
alive_sum = 0

for row in matrix:  # calculate the count and sum of all alive cells
    for el in row:
        if int(el) > 0:
            alive_count += 1
            alive_sum += int(el)

# print the output
print(f'Alive cells: {alive_count}')
print(f'Sum: {alive_sum}')

for r in matrix:
    print(' '.join(list(map(str, r))))



# Task 9
from collections import deque

size = int(input())   # read matrix size
commands = deque(input().split())   # put the command i a queue
matrix = [input().split() for r in range(size)]   # read the matrix input


collected_coals = 0   # keeps track of collected coal
coals_count = 0  # keep trak of the remaining cola
s = []  # keep the current coordinates of the miner "s"


# find the miner and count all coal
for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'c':
            coals_count += 1
        elif matrix[r][c] == 's':
            s = [r, c]
        elif matrix[r][c] == 'e':
            e = [r, c]

# assign boolean variable to keep trak whether the game is over normally or there are no mo commands
game_is_over = False

while commands:  # process the commands
    command = commands.popleft()
    if command == 'left':
        if s[1] > 0:
            s[1] -= 1
    elif command == 'right':
        if s[1] < size - 1:
            s[1] += 1
    elif command == 'up':
        if s[0] > 0:
            s[0] -= 1
    elif command == 'down':
        if s[0] < size - 1:
            s[0] += 1

    if matrix[s[0]][s[1]] == 'c':
        collected_coals += 1   # collect coal
        coals_count -= 1   # decrease the remaining coals count
        matrix[s[0]][s[1]] = '*'
        if coals_count == 0:  # the game is won!
            print(f'You collected all coal! ({s[0]}, {s[1]})')
            game_is_over = True
            break
    elif matrix[s[0]][s[1]] == 'e':  # exit the game
        print(f'Game over! ({s[0]}, {s[1]})')
        game_is_over = True
        break

if not game_is_over:  # if the game is not over but there are no more command, pint the progress status
    print(f'{coals_count} pieces of coal left. ({s[0]}, {s[1]})')


# Task 10
from collections import deque

rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]
commands = deque(input())

p = []
bunnies = set()

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == 'P':
            p = [r, c]
        elif matrix[r][c] == 'B':
            bunnies.add((r, c))


game_is_won = False

while commands:
    command = commands.popleft()
    if command == 'L':
        if p[1] == 0:
            game_is_won = True
        else:
            matrix[p[0]][p[1]] = '.'
            p[1] -= 1
            # if matrix[p[0]][p[1]] != 'B':
            matrix[p[0]][p[1]] = 'P'

    elif command == 'R':
        if p[1] == cols - 1:
            game_is_won = True
        else:
            matrix[p[0]][p[1]] = '.'
            p[1] += 1
            # if matrix[p[0]][p[1]] != 'B':
            matrix[p[0]][p[1]] = 'P'

    elif command == 'U':
        if p[0] == 0:
            game_is_won = True
        else:
            matrix[p[0]][p[1]] = '.'
            p[0] -= 1
            # if matrix[p[0]][p[1]] != 'B':
            matrix[p[0]][p[1]] = 'P'

    elif command == 'D':
        if p[0] == rows - 1:
            game_is_won = True
        else:
            matrix[p[0]][p[1]] = '.'
            p[0] += 1
            # if matrix[p[0]][p[1]] != 'B':
            matrix[p[0]][p[1]] = 'P'

    new_bunnies = set()
    for b in bunnies:
        if b[1] > 0:
            new_bunnies.add((b[0], b[1] - 1))
        if b[1] < cols - 1:
            new_bunnies.add((b[0], b[1] + 1))
        if b[0] > 0:
            new_bunnies.add((b[0] - 1, b[1]))
        if b[0] < rows - 1:
            new_bunnies.add((b[0] + 1, b[1]))

    bunnies = bunnies | new_bunnies

    for r in range(rows):
        for c in range(cols):
            if (r, c) in bunnies:
                matrix[r][c] = 'B'

    if game_is_won:
        matrix[p[0]][p[1]] = '.'
        for r in matrix:
            print(''.join(r))
        print(f"won: {p[0]} {p[1]}")
        break

    if tuple(p) in bunnies:
        for r in matrix:
            print(''.join(r))
        print(f"dead: {p[0]} {p[1]}")
        break

    # for r in matrix:
    #     print(''.join(r))
    # print()




























