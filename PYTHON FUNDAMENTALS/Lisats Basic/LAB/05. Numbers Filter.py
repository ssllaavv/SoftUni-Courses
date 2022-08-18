elements_count = int(input())

complete_list = []
filtered_list = []

for e in range(elements_count):
    complete_list.append(int(input()))

command = input()
if command == "even":
    for e in range(elements_count):
        if complete_list[e] % 2 == 0:
            filtered_list.append(complete_list[e])
if command == "odd":
    for e in range(elements_count):
        if complete_list[e] % 2 != 0:
            filtered_list.append(complete_list[e])
if command == "negative":
    for e in range(elements_count):
        if complete_list[e] < 0:
            filtered_list.append(complete_list[e])
if command == "positive":
    for e in range(elements_count):
        if complete_list[e] >= 0:
            filtered_list.append(complete_list[e])

print(filtered_list)