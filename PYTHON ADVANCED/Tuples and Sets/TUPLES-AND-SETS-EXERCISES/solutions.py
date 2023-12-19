# Task 1

n = int(input())
names_set = set()
for _ in range(n):
    names_set.add(input())
for name in names_set:
    print(name)


# Task 2
n, m = tuple(map(int, input().split()))

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())
for _ in range(m):
    m_set.add(input())

result_set = n_set & m_set
for el in result_set:
    print(el)


# Task 3

n = int(input())

elements_set = set()

for _ in range(n):
    elements = input().split()
    for el in elements:
        elements_set.add(el)

for el in elements_set:
    print(el)


# Task 4

text = input()
result = set()

for l in text:
    result.add((l, text.count(l)))

sorted_result = list(sorted(result))

for letter, count in sorted_result:
    print(f'{letter}: {count} time/s')


# Task 5

phone_book = {}
n = 0

while True:
    input_line = input().split('-')
    if input_line[0].isdigit():
        n = int(input_line[0])
        break
    name, number = input_line
    phone_book[name] = number

for _ in range(n):
    name = input()
    if name in phone_book:
        print(f'{name} -> {phone_book[name]}')
    else:
        print(f'Contact {name} does not exist.')



# Task 6

longest_intersection = set()
n = int(input())
for _ in range(n):
    first_token, second_token = input().split('-')
    first_start, first_end = [int(n) for n in first_token.split(',')]
    second_start, second_edn = [int(n) for n in second_token.split(',')]

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_edn + 1))

    intersection = first_set & second_set
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f'Longest intersection is {list(sorted(longest_intersection))} with length {len(longest_intersection)}')



# Task 7

odds = set()
evens = set()

n = int(input())
for i in range(1, n + 1):
    name = input()
    num = sum(ord(l) for l in name) // i
    if num % 2 == 0:
        evens.add(num)
    else:
        odds.add(num)

if sum(odds) == sum(evens):
    result = odds | evens
elif sum(odds) > sum(evens):
    result = odds - evens
else:
    result = odds ^ evens

print(', '.join(list(map(str, result))))



