# Test 1 - build matrix with column input
n = int(input())
matrix = []
for _ in range(n):
    matrix.append([])

for i in range(n):
    column = [int(x) for x in input().split()]
    for j in range(len(column)):
        matrix[j].append(column[j])

for r in matrix:
    print(r)

# Task 1

input_token = input().split('|')
matrix = [[int(x) for x in el.split()] for el in input_token]
flatten_matrix = [x for row in reversed(matrix) for x in row]
# print(matrix)
print(' '.join(list(map(str, flatten_matrix))))


# Task 1 - 2

input_token = input().split('|')
matrix = [[x for x in el.split()] for el in input_token]
flatten_matrix = [x for row in reversed(matrix) for x in row]
print(' '.join(flatten_matrix))


# Task 2

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command_token = input().split()
    command = command_token[0]
    if command == 'END':
        break
    r, c, v = [int(x) for x in command_token[1:]]

    if command == 'Add':
        sign = '+='
    elif command == 'Subtract':
        sign = '-='
    if r in range(n) and c in range(n):
        exec(f'matrix[r][c] {sign} v')
    else:
        print('Invalid coordinates')

for r in matrix:
    print(' '.join(list(map(str, r))))


# Task 3

n = int(input())
matrix = [list(input()) for _ in range(n)]

knights = []
most_scary_knight = None
most_scary_knight_killing_turns = 0

removed_knights_count = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'K':
            knights.append((i, j))

while True:
    for k in knights:
        possible_moves = {
            (k[0] - 2, k[1] + 1),
            (k[0] - 1, k[1] + 2),
            (k[0] + 1, k[1] + 2),
            (k[0] + 2, k[1] + 1),
            (k[0] + 2, k[1] - 1),
            (k[0] + 1, k[1] - 2),
            (k[0] - 1, k[1] - 2),
            (k[0] - 2, k[1] - 1),
        }
        killing_turns = len(set(knights) & possible_moves)

        if killing_turns > most_scary_knight_killing_turns:
            most_scary_knight_killing_turns = killing_turns
            most_scary_knight = k

    if most_scary_knight:

        # print(most_scary_knight)
        # print(most_scary_knight_killing_turns)

        matrix[most_scary_knight[0]][most_scary_knight[1]] = '0'
        knights.remove(most_scary_knight)
        removed_knights_count += 1

        # for r in matrix:
        #     print(' '.join(r))

        most_scary_knight = None
        most_scary_knight_killing_turns = 0

    else:
        break


print(removed_knights_count)
# for r in matrix:
#     print(' '.join(r))


# Task 4

size = int(input())   # read the matrix size
matrix = [[int(x) if x not in ['B', 'X'] else x for x in input().split()] for _ in range(size)]   # read matrix state


current_score = 0   # keeps the score of current direction
current_direction = None   # keeps the current direction
current_moves = []   # keeps the moves for the current direction

max_score = 0   # keeps the maximum achieved score for all directions
moves = []  # keeps the moves for the best direction


def update_max_score():
    global current_score, max_score, current_moves, moves, direction, current_direction
    if current_score > max_score:
        max_score = current_score
        moves = current_moves
        direction = current_direction
    current_score = 0
    current_moves = []
    current_direction = None


def find_the_bunny():
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'B':
                return (r, c)


bunny = find_the_bunny()  # keep the coordinates of the bunny

direction = 'right'  # keeps the best direction to go - first let's check 'right' direction
for i in range(bunny[1] + 1, size):
    if matrix[bunny[0]][i] == 'X':
        break

    max_score += matrix[bunny[0]][i]  # save right-direction score as max_score, as that is the first direction to check
    moves.append([bunny[0], i])  # save the right moves

current_direction = 'left'   # check 'left' direction
for i in range(bunny[1] - 1, -1, -1):
    if matrix[bunny[0]][i] == 'X':
        break
    current_score += matrix[bunny[0]][i]
    current_moves.append([bunny[0], i])
update_max_score()   # if max score is achieved this will save the score, moves and direction

current_direction = 'up'   # check 'up' directions
for i in range(bunny[0] - 1, -1, -1):
    if matrix[i][bunny[1]] == 'X':
        break
    current_score += matrix[i][bunny[1]]
    current_moves.append([i, bunny[1]])
update_max_score()   # if max score is achieved this will save the score, moves and direction

current_direction = 'down'   # check 'down' direction
for i in range(bunny[0] + 1, size):
    if matrix[i][bunny[1]] == 'X':
        break
    current_score += matrix[i][bunny[1]]
    current_moves.append([i, bunny[1]])
update_max_score()   # if max score is achieved this will save the score, moves and direction

# print results
print(direction)
for move in moves:
    print(move)
print(max_score)


# Task 5

size = int(input())   # read the size of the field
# read the initial state of the field
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]


def find_alice(field):
    for i in range(size):
        for j in range(size):
            if field[i][j] == 'A':
                return [i, j]


alice = find_alice(matrix)  # keeps current position of Alice
collected_eggs = 0


while True:   # start reading the commands
    command = input()
    matrix[alice[0]][alice[1]] = '*'

    if command == 'up':  # handle 'up' command
        if alice[0] == 0:
            break
        alice[0] -= 1

    elif command == 'down':  # handle 'down' command
        if alice[0] == size - 1:
            break
        alice[0] += 1

    elif command == 'right':   # handle 'right' command
        if alice[1] == size - 1:
            break
        alice[1] += 1

    elif command == 'left':  # handle 'left' command
        if alice[1] == 0:
            break
        alice[1] -= 1

    if matrix[alice[0]][alice[1]] == 'R':   # handle the case if Alice goes to rabbit
        matrix[alice[0]][alice[1]] = '*'
        break

    if matrix[alice[0]][alice[1]] not in ['.', '*']:  # check if Alice find teabags or not
        collected_eggs += matrix[alice[0]][alice[1]]
    matrix[alice[0]][alice[1]] = '*'

    if collected_eggs >= 10:   # check if the collected teabags are enough
        break


# print the result
if collected_eggs >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for r in matrix:
    print(' '.join(list(map(str, r))))



# Task 6

size = 5  # size of the square field given by requirements
matrix = [input().split() for _ in range(size)]  # read the initial state of the field


def validate_move(m):   # validate move command indexes
    if m[0] in range(size) and m[1] in range(size):
        return True
    else:
        return False


shooter = None   # keeps track of the shooter coordinates
targets = []   # keep trak of the remaining targets
shoot_targets = []   # keep trak of the shoot targets
move = []  # keeps the target coordinates specified by 'move' command

for r in range(size):  # iterate through all the coordinates of the field to find the shooter and the targets
    for c in range(size):
        if matrix[r][c] == 'A':
            shooter = [r, c]
        elif matrix[r][c] in ['x', 'X']:
            targets.append([r, c])

n = int(input())  # read the number of expected commands

for _ in range(n):   # start to process the commands
    command = input().split()
    direction = command[1]

    if command[0] == 'move':  # handle move case
        moves_count = int(command[2])
        if direction == 'left':  # handle left move case
            move = [shooter[0], shooter[1] - moves_count]
            if not validate_move(move):  # validate the move
                continue

        elif direction == 'right':  # handle  right move command
            move = [shooter[0], shooter[1] + moves_count]
            if not validate_move(move):  # validate the move
                continue

        elif direction == 'up':   # handle up move command
            move = [shooter[0] - moves_count, shooter[1]]
            if not validate_move(move):   # validate the move
                continue

        elif direction == 'down':   # handle down move command
            move = [shooter[0] + moves_count, shooter[1]]
            if not validate_move(move): # validate the move
                continue

        if move in targets:  # check if the target move field is free
            continue
        shooter = move   # position the shooter to the new position if move command was valid

    elif command[0] == 'shoot':  # handle shoot case
        if direction == 'left':  # handle left shoot
            for i in range(shooter[1] - 1, -1, -1):
                # if target is found, remove it form the targets and add it to shoot_targets
                if [shooter[0], i] in targets:
                    targets.remove([shooter[0], i])
                    shoot_targets.append([shooter[0], i])
                    break

        elif direction == 'right':   # handle right shoot
            # if target is found, remove it form the targets and add it to shoot_targets
            for i in range(shooter[1] + 1, size):
                if [shooter[0], i] in targets:
                    targets.remove([shooter[0], i])
                    shoot_targets.append([shooter[0], i])
                    break

        elif direction == 'up':   # handle up shoot
            # if target is found, remove it form the targets and add it to shoot_targets
            for i in range(shooter[0] - 1, -1, -1):
                if[i, shooter[1]] in targets:
                    targets.remove([i, shooter[1]])
                    shoot_targets.append([i, shooter[1]])
                    break

        elif direction == 'down':  # handle down shoot
            # if target is found, remove it form the targets and add it to shoot_targets
            for i in range(shooter[0] + 1, size):
                if [i, shooter[1]] in targets:
                    targets.remove([i, shooter[1]])
                    shoot_targets.append([i, shooter[1]])
                    break

    if not targets:   # if all targets are  shoot, break the cycle and print the result
        print(f'Training completed! All {len(shoot_targets)} targets hit.')
        break

if targets:  # if no more commands and the still targets left print the related message
    print(f'Training not completed! {len(targets)} targets left.')
for t in shoot_targets:  # finally, print all shoot targets
    print(t)


# Task 7

presents = int(input())   # read presents count
size = int(input())   # read size of the field
matrix = [input().split() for _ in range(size)]   # read initial state of the field


santa = []   # keep current coordinates of Santa
naughty_kind = []   # keep remaining naughty kind coordinates
nice_kids = []   # keeps remaining nice kids coordinates
cookies = []   # keeps remaining cookies coordinates

presents_for_nice_kinds = 0  # counter for presents given to nice kids


def move_santa():   # replace the previous position of Santa with empty symbol in the field
    matrix[santa[0]][santa[1]] = '-'


def place_santa():  # place the symbol for Santa to his new position in the field after he moves
    matrix[santa[0]][santa[1]] = 'S'


# find Santa, all naughty  kids. all nice kids and all cookies and stor them ti relevant variables
for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'S':
            santa = [r, c]
        elif matrix[r][c] == 'X':
            naughty_kind.append([r, c])
        elif matrix[r][c] == 'V':
            nice_kids.append([r, c])
        elif matrix[r][c] == 'C':
            cookies.append([r, c])


while presents > 0 and nice_kids:   # start executing the commands
    command = input()
    if command == 'Christmas morning':  # handel stop command
        break

    if command == 'up':  # handle  up command
        if santa[0] == 0:
            continue
        move_santa()
        santa[0] -= 1

    elif command == 'down':   # handle down command
        if santa[0] == size - 1:
            continue
        move_santa()
        santa[0] += 1

    elif command == 'left':  # handle left command
        if santa[1] == 0:
            continue
        move_santa()
        santa[1] -= 1

    elif command == 'right':   # handle right command
        if santa[1] == size - 1:
            continue
        move_santa()
        santa[1] += 1

    place_santa()  # place tSanta on its new position

    if santa in naughty_kind:  # remove the naughty kid form naughty_kids list without giving  present
        naughty_kind.remove(santa)

    elif santa in nice_kids:  # give present to the good kid and remove it form the field
        presents -= 1
        presents_for_nice_kinds += 1
        nice_kids.remove(santa)

    elif santa in cookies:  # handle cookies case
        moves = [
            [santa[0], santa[1] - 1],
            [santa[0], santa[1] + 1],
            [santa[0] - 1, santa[1]],
            [santa[0] + 1, santa[1]]
        ]
        for m in moves:
            if m in nice_kids:  # if nice kid, give present, remove the kid and increase the given presents to nice kids
                nice_kids.remove(m)
                matrix[m[0]][m[1]] = '-'
                presents -= 1
                presents_for_nice_kinds += 1
            elif m in naughty_kind:  # if naughty kid, give the present and remove the kid
                naughty_kind.remove(m)
                matrix[m[0]][m[1]] = '-'
                presents -= 1

            # if all nice kids have their presents or Santa runs out of presents, ebd the game
            if presents == 0 or not nice_kids:
                break
        cookies.remove(santa)

    # print(santa)
    # print(nice_kids)
    # print(naughty_kind)
    # for r in matrix:
    #     print(' '.join(r))


# print the result
if not presents and nice_kids:
    print('Santa ran out of presents!')
for r in matrix:
    print(' '.join(r))
if nice_kids:
    print(f'No presents for {len(nice_kids)} nice kid/s.')
else:
    print(f'Good job, Santa! {presents_for_nice_kinds} happy nice kid/s.')
