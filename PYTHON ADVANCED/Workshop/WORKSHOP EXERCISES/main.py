from math import ceil


def build_board(size):
    matrix = []
    for r in range(size):
        matrix.append([])
        for c in range(size):
            matrix[r].append(' ')
    return matrix


player_one = None
player_two = None
board = build_board(3)
loop = True


def setup():
    global player_one, player_two

    player_one_sign = None
    player_two_sign = None

    while True:
        player_one_name = input("Player one name: ")
        if player_one_name.strip().isalpha() and len(player_one_name) >= 2:
            player_one_name = player_one_name.strip()
            break
        print('Name must be at least 2 characters long and must contain only letters!')

    while True:
        player_two_name = input("Player two name : ")
        if player_two_name.strip() == player_one_name:
            print("Name must be different form player's one name")
            continue
        if player_two_name.strip().isalpha() and len(player_one_name) >= 2:
            player_two_name = player_two_name.strip()
            break
        print('Name must be at least 2 characters long and must contain only letters!')

    while True:
        player_one_sign = input(f"{player_one_name}, choose sight - 'x' or 'o': ")
        if player_one_sign.strip() in ['x', 'X']:
            player_one_sign = 'X'
            player_two_sign = 'O'
            break
        elif player_one_sign.strip() in ['0', 'o', 'O']:
            player_one_sign = 'O'
            player_two_sign = 'X'
            break
        print('Invalid input! Please, choose "x" or "o"')

    player_one = [player_two_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]

    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")
    print(f"{player_one_name} starts firs!")


setup()
current = player_one
other = player_two


def check_if_won(current, board):
    global loop

    rows = any([all(x) == current[1] for x in board])
    cols = any(all(board[x][y] == current[1] for x in range(1, 3)) for y in range(3))
    first_diagonal = all(x == current[1] for x in [board[0][0], board[1][1], board[2][2]])
    second_diagonal = all(x == current[1] for x in [board[2][0], board[1][0], board[0][2]])
    all_possible_wins = [rows, cols, first_diagonal, second_diagonal]
    if any(all_possible_wins):
        print(f"{current[0]} won!")
        loop = False


def draw_board(board):
    for row in board:
        print('| ', end="")
        print(' | '.join(([str(x) for x in row])), end="")
        print(' |')


def play(current_pl, board_setup):
    while True:
        try:
            choice = int(input(f"{current[0]}, choose a free position [1-9]: "))
            row = ceil(choice / 3) - 1
            col = choice % 3 - 1
            if board[row][col] == " ":
                board[row][col] = current[1]
                break
            else:
                print("The position is occupied. Choose, another position")
        except ValueError:
            print("Invalid input")
        except IndexError:
            print("Invalid input")

    draw_board(board)
    check_if_won(current, board)


while loop:
    play(current, board)
    current, other = other, current







