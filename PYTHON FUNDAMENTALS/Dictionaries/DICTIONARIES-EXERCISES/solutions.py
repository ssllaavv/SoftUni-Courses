# Task 1

text = input()
chars_count = {}

for char in text:
    if char != ' ' and char not in chars_count:
        chars_count[char] = 0
    if char != ' ':
        chars_count[char] += 1

for char, count in chars_count.items():
    print(f'{char} -> {count}')


# Task 2

resources = {}

while True:
    resource = input()
    if resource == 'stop':
        break

    qtt = int(input())
    if resource not in resources:
        resources[resource] = 0
    resources[resource] += qtt

for resource, qtt in resources.items():
    print(f'{resource} -> {qtt}')


# Task 3

countries = input().split(', ')
capitals = input().split(', ')

countries_capitals = dict(zip(countries, capitals))

for k, v in countries_capitals.items():
    print(f'{k} -> {v}')

# unzipped_elements = zip(*countries_capitals.items())
#
# keys, values = unzipped_elements
#
# print(keys)
# print(values)


# Task 4

phonebook = {}
search_count = 0

while True:
    command = input().split('-')
    if len(command) == 1:
        search_count = int(command[0])
        break

    name, phone_number = command
    if name not in phonebook:
        phonebook[name] = None
    phonebook[name] = phone_number

for _ in range(search_count):
    name = input()
    if name not in phonebook:
        print(f'Contact {name} does not exist.')
    else:
        print(f'{name} -> {phonebook[name]}')


# Task 5

legendary_items = {
    'shards': "Shadowmourne",
    'fragments': "Valanyr",
    'motes': "Dragonwrath",
}

materials = {
    'shards': 0,
    'fragments': 0,
    'motes': 0,
}

junk = {}

legendary_assembled = False
item = None


while not legendary_assembled:
    inputs = input().split(' ')

    for i in range(0, len(inputs), 2):
        material = inputs[i + 1].lower()
        qtt = int(inputs[i])

        if material in materials:
            materials[material] += qtt
            if materials[material] >= 250 and not legendary_assembled:
                legendary_assembled = True,
                item = legendary_items[material]
                materials[material] -= 250
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += qtt

if item:
    print(f'{item} obtained!')
for material, qtt in materials.items():
    print(f'{material}: {qtt}')
for material, qtt in junk.items():
    print(f'{material}: {qtt}')


# Task 6

products = {}

while True:
    command = input().split(' ')
    if command[0] == 'buy':
        break

    product = command[0]
    price = float(command[1])
    qtt = int(command[2])

    if product not in products:
        products[product] = {}
        products[product]['qtt'] = 0
        products[product]['price'] = 0
    products[product]['price'] = price
    products[product]['qtt'] += qtt


for p, v in products.items():
    total_price = v['price'] * v['qtt']
    print(f'{p} -> {total_price:.2f}')


# Task 7

parking = {}

n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == 'register':
        name = command[1]
        number = command[2]
        if name not in parking:
            parking[name] = number
            print(f"{name} registered {number} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[name]}")
    elif command[0] == 'unregister':
        name = command[1]
        if name in parking:
            del parking[name]
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for user, number in parking.items():
    print(f'{user} => {number}')


# Task 8

courses = {}

while True:
    command = input().split(' : ')
    if command[0] == 'end':
        break

    course, student = command
    if course not in courses:
        courses[course] = []
    courses[course].append(student)

for course, students in courses.items():
    print(f'{course}: {len(students)}')
    for student in students:
        print(f'-- {student}')


# Rask 9

students = {}

n = int(input())

for _ in range(n):
    student = input()
    grade = float(input())
    if student not in students:
        students[student] = []
    students[student].append(grade)

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        print(f'{student} -> {average_grade:.2f}')


# Task 10

companies = {}

while True:
    command = input().split(' -> ')
    if command[0] == 'End':
        break

    company, employee = command
    if company not in companies:
        companies[company] = []
    if employee not in companies[company]:
        companies[company].append(employee)

for c, e in companies.items():
    print(c)
    for id_num in e:
        print(f"-- {id_num}")


# Task 11

sides_and_users = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    all_users = []
    for v in sides_and_users.values():
        all_users.extend(v)

    if ' | ' in command:
        side, user = command.split(' | ')
        if user not in all_users and side not in sides_and_users:
            sides_and_users[side] = [user]
        elif user not in all_users and side in sides_and_users:
            sides_and_users[side].append(user)

    if ' -> ' in command:
        user, side = command.split(' -> ')
        if side not in sides_and_users:
            sides_and_users[side] = []
        for s in sides_and_users.keys():
            if user in sides_and_users[s]:
                sides_and_users[s].remove(user)
        sides_and_users[side].append(user)

        print(f"{user} joins the {side} side!")

for side, users in sides_and_users.items():
    if users:
        print(f'Side: {side}, Members: {len(sides_and_users[side])}')
        for user in users:
            print(f'! {user}')


# Task 12

exams = {}
banned_students = []

while True:
    command = input().split('-')
    if command[0] == 'exam finished':
        break

    if command[1] == 'banned':
        banned_students.append(command[0])
    else:
        student, language, score = command
        if language not in exams:
            exams[language] = [{'submissions': 0}, {}]
        if student not in exams[language][1]:
            exams[language][1][student] = int(score)
        else:
            exams[language][1][student] = max(int(score), exams[language][1][student])
        exams[language][0]['submissions'] += 1

print('Results:')
for students_scores in exams.values():
    for student, score in students_scores[1].items():
        if student not in banned_students:
            print(f'{student} | {score}')

print('Submissions:')
for language, submissions in exams.items():
    print(f'{language} - {submissions[0]["submissions"]}')
