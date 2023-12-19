# Task 1
numbers = tuple(map(float, input().split()))
set_of_numbers = {n for n in numbers}

for n in numbers:
    if n in set_of_numbers:
        set_of_numbers.remove(n)
        print(f'{n} - {numbers.count(n)} times')


# Task 1 - 2
numbers = tuple(map(float, input().split()))
numbers_dict = {}
for n in numbers:
    if n not in numbers_dict:
        numbers_dict[n] = 0
    numbers_dict[n] += 1

for number, times in numbers_dict.items():
    print(f'{number} - {times} times')


# Task 2
n = int(input())
students = {}

for _ in range(n):
    student, grade = tuple(input().split())
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for s, g in students.items():
    avd_grade = sum(g) / len(g)
    grades = ''
    for grade in g:
        grades += f' {grade:.2f}'
    print(f'{s} ->{grades} (avg: {avd_grade:.2f})')


# Task 3

n = int(input())
unique_names = set()
for _ in range(n):
    unique_names.add(input())
for name in unique_names:
    print(name)


# Task 4
n = int(input())
cars = set()

for _ in range(n):
    command, car = tuple(input().split(', '))
    if command == 'IN':
        cars.add(car)
    elif command == 'OUT':
        if car in cars:
            cars.remove(car)
if cars:
    for car in cars:
        print(car)
else:
    print('Parking Lot is Empty')


# Task 5
invited = set()
coming = set()

list_length = int(input())

for _ in range(list_length):
    invited.add(input())

while True:
    guest = input()
    if guest == 'END':
        break
    coming.add(guest)

not_coming = invited - coming
sorted_not_coming = tuple(sorted(not_coming))

print(len(not_coming))
for person in sorted_not_coming:
    print(person)


# Task 6
numbers = list(map(int, input().split()))
target = int(input())
while numbers:
    for i in range(len(numbers)):
        if target - numbers[i] in numbers:
            if (target - numbers[i] == numbers[i] and numbers.count(numbers[i] > 1)) \
                    or target - numbers[i] != numbers[i] :
                print(f'{numbers[i]} + {target - numbers[i]} = {target}')
                numbers.remove(target - numbers[i])
                numbers.remove(numbers[i])
                break
    else:
        break

























