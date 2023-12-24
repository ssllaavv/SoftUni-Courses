n, m = [int(el) for el in input().split()]

matrix = []
for _ in range(n):
    matrix.append(list(input()))

commands = list(input())

won = False
dead = False

player_pos = []
for r in range(n):
    for c in range(m):
        if matrix[r][c] == "P":
            player_pos = [r, c]
            break
    if player_pos:
        break

while commands:
    command = commands.pop(0)
    bunnies_pos = []
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == "B":
                bunnies_pos.append([r, c])







    if command == "R":
        if player_pos[1] == m - 1:
            won = True
            matrix[player_pos[0]][player_pos[1]] = "."

        else:
            if matrix[player_pos[0]][player_pos[1] + 1] == "B":
                dead = True
                player_pos[1] += 1

            else:
                matrix[player_pos[0]][player_pos[1] + 1] = "P"
                matrix[player_pos[0]][player_pos[1]] = "."
                player_pos[1] += 1

    elif command == "L":
        if player_pos[1] == 0:
            won = True
            matrix[player_pos[0]][player_pos[1]] = "."

        else:
            if matrix[player_pos[0]][player_pos[1] - 1] == "B":
                dead = True
                player_pos[1] -= 1

            else:
                matrix[player_pos[0]][player_pos[1] - 1] = "P"
                matrix[player_pos[0]][player_pos[1]] = "."
                player_pos[1] -= 1

    elif command == "U":
        if player_pos[0] == 0:
            won = True
            matrix[player_pos[0]][player_pos[1]] = "."

        else:
            if matrix[player_pos[0] - 1][player_pos[1]] == "B":
                dead = True
                player_pos[0] -= 1

            else:
                matrix[player_pos[0] - 1][player_pos[1]] = "P"
                matrix[player_pos[0]][player_pos[1]] = "."
                player_pos[0] -= 1

    elif command == "D":
        if player_pos[0] == n - 1:
            won = True
            matrix[player_pos[0]][player_pos[1]] = "."

        else:
            if matrix[player_pos[0] + 1][player_pos[1]] == "B":
                dead = True
                player_pos[0] += 1

            else:
                matrix[player_pos[0] + 1][player_pos[1]] = "P"
                matrix[player_pos[0]][player_pos[1]] = "."
                player_pos[0] += 1




    while bunnies_pos:
        bunny = bunnies_pos.pop()
        if bunny[1] < m - 1:
            matrix[bunny[0]][bunny[1] + 1] = "B"
        if bunny[1] > 0:
            matrix[bunny[0]][bunny[1] - 1] = "B"
        if bunny[0] < n - 1:
            matrix[bunny[0] + 1][bunny[1]] = "B"
        if bunny[0] > 0:
            matrix[bunny[0] - 1][bunny[1]] = "B"


    still_there_is_player = False
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == "P":
                still_there_is_player = True
                break
        if still_there_is_player:
            break
    if not still_there_is_player:
        dead = True
        break
    if won or dead:
        break





    # for r_ in range(n):
    #     print(*matrix[r_])
    # print()

for r_ in range(n):
    print(*matrix[r_], sep="")
if won:
    print("won:", end=" ")
    print(*player_pos)
elif dead:
    print("dead:", end=" ")
    print(*player_pos)
