from color_test import colors


matrix = [[0 for _ in range(7)] for _ in range(6)]


def print_matrix():

    for row in matrix:
        print()
        for col in row:
            if col == 1:
                print(colors.RED + str(col) + colors.RESET, end=" ")
            elif col == 2:
                print(colors.BLUE + str(col) + colors.RESET, end=" ")
            else:
                print(col, end=" ")


pl_one_turns = []
pl_two_turns = []

pl_one_wins = False
pl_two_wins = False

while True:

    pl_one_turn_not_allowed = True
    pl_two_turn_not_allowed = True

    while pl_one_turn_not_allowed:
        try:
            pl_one_column = int(input('Player 1, please choose column: '))

            if 1 <= pl_one_column <= 7:
                for r in range(5, -1, -1):
                    if matrix[r][pl_one_column - 1] == 0:
                        matrix[r][pl_one_column - 1] = 1
                        pl_one_turns.append((r, pl_one_column - 1))
                        pl_one_turn_not_allowed = False
                        break
            if pl_one_turn_not_allowed:
                print("Invalid column selection, please choose another column")
        except ValueError:
            print("Invalid column selection, please choose another column")

    print_matrix()

    while pl_two_turn_not_allowed:
        try:
            pl_two_column = int(input('Player 2, please choose column: '))

            if 1 <= pl_two_column <= 7:
                for r in range(5, -1, -1):
                    if matrix[r][pl_two_column - 1] == 0:
                        matrix[r][pl_two_column - 1] = 2
                        pl_two_turns.append((r, pl_two_column - 1))
                        pl_two_turn_not_allowed = False
                        break
            if pl_two_turn_not_allowed:
                print("Invalid column selection, please choose another column")
        except ValueError:
            print("Invalid column selection, please choose another column")

    print_matrix()

    # Check for winner

    if len(pl_one_turns) >= 4 and len(pl_two_turns) >= 4:
        pl_one_last_turns = pl_one_turns[-4:]
        pl_two_last_turns = pl_two_turns[-4:]

        pl_one_last_turns_sorted = list(sorted(pl_one_last_turns, key=lambda x: (x[0], x[1])))
        pl_two_last_turns_sorted = list(sorted(pl_two_last_turns, key=lambda x: (x[0], x[1])))

        print(pl_one_last_turns_sorted)
        print(pl_two_last_turns_sorted)

        # Check first player
        first_el_pl_one_row = pl_one_last_turns_sorted[0][0]
        first_el_pl_one_col = pl_one_last_turns_sorted[0][1]

        all_first_rows_are_equal = all(x[0] == first_el_pl_one_row for x in pl_one_last_turns_sorted)
        all_first_cols_are_equal = all(x[1] == first_el_pl_one_col for x in pl_one_last_turns_sorted)

        all_first_rows_are_consecutive = all(
            pl_one_last_turns_sorted[i][0] == pl_one_last_turns_sorted[i - 1][0] + 1 for i in range(1, 4))
        all_first_cols_are_consecutive = (
            all(pl_one_last_turns_sorted[i][1] == pl_one_last_turns_sorted[i - 1][1] + 1 for i in range(1, 4)) or
            all(pl_one_last_turns_sorted[i][1] == pl_one_last_turns_sorted[i - 1][1] - 1 for i in range(1, 4)))

        if (all_first_rows_are_equal and all_first_cols_are_consecutive) or \
                (all_first_cols_are_equal and all_first_rows_are_consecutive) or \
                (all_first_rows_are_consecutive and all_first_cols_are_consecutive):
            pl_one_wins = True

        # Check second player
        first_el_pl_two_row = pl_two_last_turns_sorted[0][0]
        first_el_pl_two_col = pl_two_last_turns_sorted[0][1]

        all_second_rows_are_equal = all(x[0] == first_el_pl_two_row for x in pl_two_last_turns_sorted)
        all_second_cols_are_equal = all(x[1] == first_el_pl_two_col for x in pl_two_last_turns_sorted)

        all_second_rows_are_consecutive = all(
            pl_two_last_turns_sorted[i][0] == pl_two_last_turns_sorted[i - 1][0] + 1 for i in range(1, 4))
        all_second_cols_are_consecutive = (
                all(pl_two_last_turns_sorted[i][1] == pl_two_last_turns_sorted[i - 1][1] + 1 for i in range(1, 4)) or
                all(pl_two_last_turns_sorted[i][1] == pl_two_last_turns_sorted[i - 1][1] - 1 for i in range(1, 4)))

        if (all_second_rows_are_equal and all_second_cols_are_consecutive) or \
                (all_second_cols_are_equal and all_second_rows_are_consecutive) or \
                (all_second_rows_are_consecutive and all_second_cols_are_consecutive):
            pl_two_wins = True

        # Print winner, if winner
        if pl_one_wins and pl_two_wins:
            print("Draw!")
            print(f"Player 1: {pl_one_last_turns_sorted}")
            print(f"Player 2: {pl_two_last_turns_sorted}")
            print_matrix()
            break
        elif pl_one_wins:
            print("Player 1 wins!")
            print(f"Player 1: {pl_one_last_turns_sorted}")
            print_matrix()
            break
        elif pl_two_wins:
            print("Player 2 wins!")
            print(f"Player 2: {pl_two_last_turns_sorted}")
            print_matrix()
            break
