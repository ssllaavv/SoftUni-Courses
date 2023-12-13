# Task 1

decimal_num = int(input())
binary_num = int(input())

decimal_to_binary = []

result = decimal_num
while result > 0:
    reminder = result % 2
    result = result // 2
    decimal_to_binary.insert(0, reminder)

print(decimal_to_binary.count(binary_num))


# Task 2

number = int(input())
number = number >> 1
print(number & 1)


# Task 3

number = int(input())
position = int(input())
number = number >> position
print(number & 1)


# Task 4

def convert_int_to_binary(n):
    decimal_to_binary = ""
    temp_num = n
    while temp_num > 0:
        reminder = temp_num % 2
        temp_num = temp_num // 2
        decimal_to_binary = str(reminder) + decimal_to_binary

    return int(decimal_to_binary)


number = int(input())
position = int(input())
mask = ~(1 << position)

result = number & mask
number_b = int(convert_int_to_binary(number))
result_b = int(convert_int_to_binary(result))


print(f'{number} -> {result}')
print(f"{number_b} -> {result_b}")


# Task 5

numbers_list = list(map(int, input().split(' ')))
result = 0
for n in numbers_list:
    result = result ^ n

print(result)


# Task 6

number = int(input())
position = int(input())

mask = 7 << position
result = number ^ mask

def convert_int_to_binary(n):
    decimal_to_binary = ""
    temp_num = n
    while temp_num > 0:
        reminder = temp_num % 2
        temp_num = temp_num // 2
        decimal_to_binary = str(reminder) + decimal_to_binary

    return int(decimal_to_binary)


print(f'{number} -> {result}')
print(f'{convert_int_to_binary(number)} -> {convert_int_to_binary(result)}')

































