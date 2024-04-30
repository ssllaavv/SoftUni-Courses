def print_row(size, stars_count):
    for row in range(size - stars_count):
        print(" ", end="")
    for row in range(1, stars_count):
        print("* ", end="")
    print("*")


size = int(input())

for stars_count in range(1, size):
    print_row(size, stars_count)
for stars_count in range(size, 0, -1):
    print_row(size, stars_count)

