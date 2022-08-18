size = int(input())

for i in range(1, size + 1):
    for j in range(i):
        print("*", end='')
    print()

for i in range(size - 1, 0, -1):
    for j in range(i):
        print("*", end='')
    print()

