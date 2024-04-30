def print_triangle(size: int):
    for r in range(size):
        for c in range(r + 1):
            print(c + 1, end=" ")
        print()
    for r in range(size - 2, -1, -1):
        for c in range(r + 1):
            print(c + 1, end=" ")
        print()

