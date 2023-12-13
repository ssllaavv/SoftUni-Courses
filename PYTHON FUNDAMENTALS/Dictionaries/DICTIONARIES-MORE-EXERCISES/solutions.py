# Task 1
#
contests = {}
students = {}

best_student = None
max_points = 0

while True:
    command = input()
    if command == 'end of contests':
        break

    contest, password = command.split(':')
    contests[contest] = password

while True:
    command = input()
    if command == 'end of submissions':
        break

    contest, password, user, points = command.split('=>')
    if password == contests.get(contest):
        if user not in students:
            students[user] = {}
        if contest not in students[user]:
            students[user][contest] = 0
        if int(points) > students[user][contest]:
            students[user][contest] = int(points)

for student, contests in students.items():
    students_score = 0
    for contest, points in contests.items():
        students_score += points
    if students_score > max_points:
        best_student = student
        max_points = students_score

print(f'Best candidate is {best_student} with total {max_points} points.')
print("Ranking:")
for student, contests in sorted(students.items()):
    print(student)
    for contest, score in sorted(contests.items(), key=lambda x: x[1], reverse=True):
        print(f'#  {contest} -> {score}')


# Task 2

contests_dict = {}
students_dict = {}

while True:
    command = input()
    if command == 'no more time':
        break

    student, contest, score = command.split(' -> ')
    if student not in students_dict:
        students_dict[student] = {}
    if contest not in students_dict[student]:
        students_dict[student][contest] = 0
    if int(score) >= students_dict[student][contest]:
        students_dict[student][contest] = int(score)

    if contest not in contests_dict:
        contests_dict[contest] = {}
    if student not in contests_dict[contest]:
        contests_dict[contest][student] = 0
    if int(score) > contests_dict[contest][student]:
        contests_dict[contest][student] = int(score)

for student, contests in students_dict.items():
    total_score = 0
    for score in contests.values():
        total_score += score
    students_dict[student]['total_score'] = total_score

for contest, students in contests_dict.items():
    print(f'{contest}: {len(students.keys())} participants')
    for number, (student, score) in enumerate(sorted(students.items(), key=lambda x: (-x[1], x[0])), 1):
        print(f'{number}. {student} <::> {score}')

print('Individual standings:')

students_dict = dict(sorted(students_dict.items(), key=lambda x: (-x[1]['total_score'], x[0])))
for number, student in enumerate(students_dict.keys(), 1):
    print(f'{number}. {student} -> {students_dict[student]["total_score"]}')


# Task 3

players_dict = {}

while True:
    command = input()
    if command == 'Season end':
        break

    if ' -> ' in command:
        player, position, skill = command.split(' -> ')
        if player not in players_dict:
            players_dict[player] = {}
        if position not in players_dict[player]:
            players_dict[player][position] = 0
        if int(skill) > players_dict[player][position]:
            players_dict[player][position] = int(skill)

    elif ' vs ' in command:
        pl_1, pl_2 = command.split(' vs ')
        if players_dict.get(pl_1) and players_dict.get(pl_2):
            pl_1_skills_set = set(players_dict[pl_1].keys())
            pl_2_skills_set = set(players_dict[pl_2].keys())
            common_positions = pl_1_skills_set & pl_2_skills_set
            if common_positions:
                pl_1_total_skills = 0
                pl_2_total_skills = 0

                for p in common_positions:
                    pl_1_total_skills += players_dict[pl_1][p]
                    pl_2_total_skills += players_dict[pl_2][p]

                if pl_1_total_skills > pl_2_total_skills:
                    del players_dict[pl_2]
                elif pl_1_total_skills < pl_2_total_skills:
                    del players_dict[pl_1]

for pl, positions in players_dict.items():
    total_points = 0
    for s in positions.values():
        total_points += s
    players_dict[pl]['total_points'] = total_points

players_dict = dict(sorted(players_dict.items(), key=lambda x: (-x[1]['total_points'], x[0])))

for p, info in players_dict.items():
    print(f"{p}: {players_dict[p]['total_points']} skill")

    info = dict(sorted(info.items(), key=lambda x: (-x[1], x[0])))
    for pos, skill in info.items():
        if pos != 'total_points':
            print(f'- {pos} <::> {skill}')


# Task 4

dwarfs = {}

while True:
    command = input()
    if command == 'Once upon a time':
        break

    name, color, physics = command.split(' <:> ')
    if (name, color) not in dwarfs:
        dwarfs[(name, color)] = int(physics)
    else:
        dwarfs[(name, color)] = max(int(physics), dwarfs[(name, color)])


def custom_sort(item):
    name, color = item[0]
    physics = item[1]
    count_same_color = sum(1 for key in dwarfs if key[1] == color)
    return (-physics, -count_same_color)


dwarfs = dict(sorted(dwarfs.items(), key=custom_sort))


for dwarf in dwarfs.items():
    print(f'({dwarf[0][1]}) {dwarf[0][0]} <-> {dwarf[1]}')



# Task 5

dragons = {}

n = int(input())
for _ in range(n):
    dragon_type, name, damage, health, armo = input().split(' ')
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armo == "null":
        armo = 10

    if dragon_type not in dragons:
        dragons[dragon_type] = {}
    dragons[dragon_type][name] = (int(damage), int(health), int(armo))

for group, drags in dragons.items():
    sorted_dragons = tuple(sorted(drags.items(), key=lambda x: x[0]))
    averages = tuple(sum(x) / len(sorted_dragons) for x in
                     zip(*[stats for _, stats in sorted_dragons]))

    print(f'{group}::({averages[0]:.2f}/{averages[1]:.2f}/{averages[2]:.2f})')

    for drag in sorted_dragons:
        print(f'-{drag[0]} -> '
              f'damage: {drag[1][0]}, '
              f'health: {drag[1][1]}, '
              f'armor: {drag[1][2]}')































