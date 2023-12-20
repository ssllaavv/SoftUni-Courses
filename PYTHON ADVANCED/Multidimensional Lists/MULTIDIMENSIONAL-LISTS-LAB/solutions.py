# Test 1

matrix = []
for i in range(3):
    matrix.append([])
    for j in range(4):
        matrix[i].append(0)

print(matrix)


# Test 2

matrix = []
for i in range(3):
    matrix.append([])
    for j in range(4):
        matrix[i].append(i * j)

print(matrix)


# Test 3
matrix_1 = [[0 for j in range(2)] for i in range(3)]
print(matrix_1)

matrix_2 = [[j for j in range(1, 4)] for i in range(4)]
print(matrix_2)

matrix_3 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
flatten_matrix_3 = [n for line in matrix_3 for n in line]
print(flatten_matrix_3)


# Test 4
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

[print(el) for el in [row for row in matrix]]

# Test 5

matrix = []

for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append([])
        for k in range(3):
            matrix[i][j].append(k + 1)

flatten_matrix = [n for d_1 in matrix for d_2 in d_1 for n in d_2]

print(matrix)
print(flatten_matrix)



# Task 1

rows, cols = list(map(int, input().split(', ')))
matrix = []
sum_of_all_elements = 0

for i in range(rows):
    matrix.append(list(map(int, input().split(', '))))
    sum_of_all_elements += sum(matrix[i])

print(sum_of_all_elements)
print(matrix)


# Task 2

rows = int(input())
matrix = []

for i in range(rows):
    matrix.append(list(filter(lambda x: x % 2 == 0, (map(int, input().split(', '))))))

print(matrix)



# Task 3

rows = int(input())
matrix = [list(map(int, input().split(', '))) for _ in range(rows)]
flatten_matrix = [el for row in matrix for el in row]

print(flatten_matrix)


# Task 4

rows, cols = list(map(int, input().split(', ')))

matrix = []
for i in range(rows):
    matrix.append(list(map(int, input().split(' '))))

result = []
for c in range(cols):
    column_sum = 0
    for r in range(rows):
        column_sum += matrix[r][c]
    result.append(column_sum)

[print(n) for n in result]


# Task 5

n = int(input())
matrix = [[int(x) for x in input().split()] for i in range(n)]
print(sum([matrix[i][i] for i in range(n)]))


# Task 6
size = int(input())
matrix = [[x for x in list(input())] for i in range(size)]
symbol = input()
result = [(x, y) for x in range(size) for y in range(size) if matrix[x][y] == symbol]

if result:
    print(result[0])
else:
    print(f'{symbol} does not occur in the matrix')


# Task 7

rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(n) for n in input().split(', ')] for _ in range(rows)]

max_sum = 0
sub_matrix = []

for i in range(rows - 1):
    for j in range(cols - 1):
        result = 0
        row_1 = [matrix[i][j], matrix[i][j + 1]]
        row_2 = [matrix[i + 1][j], matrix[i + 1][j + 1]]
        result += sum(row_1) + sum(row_2)
        if result > max_sum:
            max_sum = result
            sub_matrix = [row_1, row_2]

for row in sub_matrix:
    print(f'{row[0]} {row[1]}')
print(max_sum)























