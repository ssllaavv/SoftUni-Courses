# # Task 1
#
# # read the inputs
# population = list(map(int, input().split(', ')))
# min_wealth = int(input())
#
# # start to redistribute the wealth form the richest to the poorest (Vive le communisme!)
# while not all(x >= min_wealth for x in population):  # check if there are still poor people left
#     min_index = population.index(min(population))
#
#     if max(population) <= min_wealth:  # check if there is enough wealth redistribute
#         break
#
#     # check if there are still poor people and there are still rich enough people to takem wealth from
#     while population[min_index] < min_wealth and max(population) > min_wealth:
#
#         max_index = population.index(max(population))
#
#         needed_amount = min_wealth - population[min_index]
#
#         if population[max_index] - needed_amount < min_wealth:
#             amount_possible = population[max_index] - min_wealth
#             population[min_index] += amount_possible
#             population[max_index] = min_wealth
#         else:
#             population[max_index] -= needed_amount
#             population[min_index] = min_wealth
#
# if min(population) >= min_wealth:  # we've acHived communism !
#     print(population)
# else:
#     print('No equal distribution possible')  # stick to capitalism


# # Task 2
#
# text = input()
#
# numbers = []
# strings = []
#
# for el in text:
#     if not el.isdigit():
#         strings.append(el)
#     elif el.isdigit():
#         numbers.append(int(el))
#
# take = []
# skip = []
#
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         take.append(numbers[i])
#     else:
#         skip.append(numbers[i])
#
#
# result = ''
#
# for i in range(len(numbers) // 2):
#     for n in range(take.pop(0)):
#         if strings:
#             result += strings.pop(0)
#
#     for n in range(skip.pop(0)):
#         if strings:
#             strings.pop(0)
#
# print(result)

#
# # Task 3
#
# rows_count = int(input())
#
# maze = []
# moves = []
# moves_count = 0
# brunch_points = []
# k = []
# branches = []
# next_move_wins = False
# possible_moves = []
#
#
# for _ in range(rows_count):
#     maze.append(list(input()))
#
# columns_count = len(maze[0])
#
#
# def find_kate(matrix):
#     kate = None
#
#     for r in range(rows_count):
#         if kate:
#             break
#         for c in range(columns_count):
#             if matrix[r][c] == 'k':
#                 kate = [r, c]
#                 break
#
#     return kate
#
#
# def check_if_possible_moves(maze, k):
#     next_move_wins = False
#
#     all_moves = [
#         [k[0], k[1] - 1],
#         [k[0], k[1] + 1],
#         [k[0 - 1], k[1]],
#         [k[0 + 1], k[1]]
#     ]
#
#     inside_moves = [m for m in all_moves
#                     if 0 <= m[0] < len(matrix) and
#                     0 <= m[1] < len(matrix[0])]
#
#     if len(inside_moves) < 4:
#         next_move_wins = True
#
#     possible_moves = [m for m in inside_moves if maze[m[0]][m[1]] == ' ']
#
#     return possible_moves, next_move_wins
#
#
# def make_move(maze, k, possible_moves, moves_count, branch_points):
#     branch_point = None
#
#     if len(possible_moves) == 1:
#         maze[k[0]][k[1]] = '.'
#         maze[possible_moves[0][0]][possible_moves[0][1]] = 'k'
#         k = maze[possible_moves[0][0]][possible_moves[0][1]]
#         moves_count += 1
#         moves. append(k)
#
#     else:
#         branch_points.append(k)
#         branch_move = possible_moves[0]
#         maze[k[0]][k[1]] = '.'
#         maze[branch_move[0]][branch_move[1]] = 'k'
#         k = maze[branch_move[0]][branch_move[1]]
#         moves_count += 1
#
#     return maze, k, moves_count, branch_points
#
#
# k = find_kate(matrix=maze)
#
# possible_moves, next_move_wins = check_if_possible_moves(maze, k)
#
# while True:
#     if not possible_moves and next_move_wins:
#         moves_count += 1
#         break
#     if not possible_moves and not next_move_wins:
#         print('Kate cannot get out')
#         break
#
#     move = make_move(maze, k, possible_moves, moves)
#
#     matrix, k, moves_count, branch_move = move
#
#     branches.append(branch_move)
#
#     possible_moves, next_move_wins = check_if_possible_moves(maze, k)
#
#     for r in maze:
#         print(r)


# # Task 4
#
# n = int(input())
# matrix = []
# destroyed_ships = 0
#
# for r in range(n):
#     matrix.append(list(map(int, input().split(' '))))
#
# command_line = input().split(' ')
# commands = [[int(c[0]), int(c[2])] for c in command_line]
#
# for c in commands:
#     if matrix[c[0]][c[1]] > 0:
#         matrix[c[0]][c[1]] -= 1
#         if matrix[c[0]][c[1]] == 0:
#             destroyed_ships += 1
#
# print(destroyed_ships)


# Task 5

# read size of the matrix (rows count)
rows = int(input())

# assign variables
matrix = []
all_dots = []  # keep the coordinate of all dots
checked_dots = []   # keep trak of all dots that was thoroughly checked for neighbouring connections
max_connected_dots = 0  # keep trak of maximum achieved connectio dots
max_connected_dots_coordinates = []  # it will save the coordinates of the maximum connected dots fount (not required!)

connected_dots = []  # keep trak of all newly found connected dots, that are not yet thoroughly checked

# Build the matrix
for _ in range(rows):
    matrix.append(input().split(' '))

# measure the columns
cols = len(matrix[0])

# find the coordinates of all dots
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == '.':
            all_dots.append([r, c])


# separate logic fo checking the neighbours for connection in a function
def check_for_connected_dots():
    global dot
    global connected_dots

    if [dot[0] - 1, dot[1]] in all_dots and [dot[0] - 1, dot[1]] not in checked_dots:
        connected_dots.append([dot[0] - 1, dot[1]])
    if [dot[0] + 1, dot[1]] in all_dots and [dot[0] + 1, dot[1]] not in connected_dots:
        connected_dots.append([dot[0] + 1, dot[1]])
    if [dot[0], dot[1] - 1] in all_dots and [dot[0], dot[1] - 1] not in connected_dots:
        connected_dots.append([dot[0], dot[1] - 1])
    if [dot[0], dot[1] + 1] in all_dots and [dot[0], dot[1] + 1] not in connected_dots:
        connected_dots.append([dot[0], dot[1] + 1])
    checked_dots.append(dot)


# start to check for connections frm the first found dot in the matrix
while all_dots:

    connected_dots = []
    dot = all_dots.pop(0)
    connected_dots.append(dot)
    check_for_connected_dots()

    while True:

        unchecked_dots = []  # keep trak of unchecked connected dots

        for d in connected_dots:
            if d not in checked_dots:
                unchecked_dots.append(d)

        if not unchecked_dots:
            break

        for dot in unchecked_dots:
            all_dots.remove(dot)
            check_for_connected_dots()

    if len(connected_dots) > max_connected_dots:
        max_connected_dots = len(connected_dots)
        max_connected_dots_coordinates = connected_dots

# otput the result
print(max_connected_dots)
# print(max_connected_dots_coordinates)






















