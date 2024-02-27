from color_test import colors
from collections import deque

matrix = []
rows = 0
cols = 0
players_count = 0
pl_turns = []
player_wins = []


# Set different color for each player
def set_color(pl: int):
    if pl == 1:
        return colors.ONE
    elif pl == 2:
        return colors.TWO
    elif pl == 3:
        return colors.THREE
    elif pl == 4:
        return colors.FOUR
    elif pl == 5:
        return colors.FIVE
    elif pl == 0:
        return colors.WHITE


# Read and validate all the inputs form the console - rows, columns, players count
def set_game():
    global rows, cols, players_count, pl_turns, player_wins

    print("Please, enter game board size")
    while True:  # read size rows
        try:
            rows = int(input("Enter rows number between 5 and 20: "))
        except ValueError:
            ...
        if 5 <= rows <= 20:
            break
        else:
            print('Invalid input')

    while True:  # read size -  columns
        try:
            cols = int(input("Enter columns number between 5 and 20: "))
        except ValueError:
            ...
        if 5 <= cols <= 20:
            break
        else:
            print('Invalid input')

    while True:  # read players count
        try:
            players_count = int(input("Please, enter players count between 2 and 5: "))
        except ValueError:
            ...
        if 2 <= players_count <= 5:
            break
        else:
            print("Invalid input")

    pl_turns = [deque() for _ in range(players_count)]  # prepare list of queues according players count
    player_wins = [0 for _ in range(players_count)]  # prepare a list to keep the state of players wins


def build_matrix():
    global matrix, rows, cols
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]


def print_matrix():  # print the matrix with different color for each player
    for row in matrix:
        for p in row:
            clr = set_color(p)
            print(clr + str(p) + colors.RESET, end=" ")
        print()


def check_more_turns_are_possible():  # check if there is still empty places to make turns
    global matrix, players_count
    free_positions = 0
    for r in matrix:
        for c in r:
            if c == 0:
                free_positions += 1
    if free_positions >= players_count:
        return True
    return False


# make turn,  place the player number in the matrix and keep trak for the last four moves for each player
def players_makes_turns():
    global players_count, rows, cols, pl_turns
    for pl in range(1, players_count + 1):
        clr = set_color(pl)
        pl_turn_not_allowed = True

        while pl_turn_not_allowed:

            try:
                pl_column = int(input(clr + f'Player {pl}, please choose column: ' + colors.RESET))

                if 1 <= pl_column <= cols:
                    for r in range(rows - 1, -1, -1):
                        if matrix[r][pl_column - 1] == 0:
                            matrix[r][pl_column - 1] = pl
                            pl_turns[pl - 1].append((r, pl_column - 1))
                            if len(pl_turns[pl - 1]) > 4:
                                pl_turns[pl - 1].popleft()
                            pl_turn_not_allowed = False
                            break
                if pl_turn_not_allowed:
                    print("Invalid column selection, please choose another column")
            except ValueError:
                print("Invalid column selection, please choose another column")
        print_matrix()


def check_for_winner():
    global matrix, pl_turns, player_wins

    if len(pl_turns[-1]) >= 4:

        for pl in range(1, len(pl_turns) + 1):  # iterate trough each players last 4 moves
            pl_turns_sorted = list(sorted(pl_turns[pl - 1], key=lambda x: (x[0], x[1])))  # sort the movee ascending

            pl_row = pl_turns_sorted[0][0]  # find the row of the first coordinate form sorted moves
            pl_col = pl_turns_sorted[0][1]  # find the column of the first coordinate form sorted moves

            all_rows_are_equal = all(x[0] == pl_row for x in pl_turns_sorted)  # check for horizontal  match
            all_cols_are_equal = all(x[1] == pl_col for x in pl_turns_sorted)  # check for vertical match

            # check if first diagonal match condition is met (consecutive coordinates for rows)
            all_rows_are_consecutive = all(
                pl_turns_sorted[i][0] == pl_turns_sorted[i - 1][0] + 1 for i in range(1, 4))

            # check if second diagonal condition is met (consecutive coordinates for columns)
            all_cols_are_consecutive = (
                    all(pl_turns_sorted[i][1] == pl_turns_sorted[i - 1][1] + 1 for i in range(1, 4)) or
                    all(pl_turns_sorted[i][1] == pl_turns_sorted[i - 1][1] - 1 for i in range(1, 4)))

            # check if win case satisfied and register in player_wins list
            if (all_rows_are_equal and all_cols_are_consecutive) or \
                    (all_cols_are_equal and all_rows_are_consecutive) or \
                    (all_rows_are_consecutive and all_cols_are_consecutive):
                player_wins[pl - 1] = 1

    if any(player_wins):
        return True
    return False


def print_result():
    if any(player_wins):
        for p in range(len(player_wins)):
            if player_wins[p] == 1:
                clr = set_color(p + 1)
                print(clr + f"Player {p + 1} wins! Moves: {[c for c in pl_turns[p]]}" + colors.RESET)
    else:
        print('GAME OVER!\nNobody wins!')


set_game()  # read initial inputs
build_matrix()  # build matrix
print_matrix()  # print initial matrix state - all zeroes

# until there is no winner and there are empty positions, the players make turns
while check_more_turns_are_possible() and not check_for_winner():
    players_makes_turns()

# print the result
print_result()
