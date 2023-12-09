# # Task 1
#
# energy = int(input())
# won_battles_count = 0
#
# while True:
#     command = input()
#     if command == 'End of battle':
#         print(f'Won battles: {won_battles_count}. Energy left: {energy}')
#         break
#     else:
#         enemy_distance = int(command)
#         if energy - enemy_distance >= 0:
#             energy -= enemy_distance
#             won_battles_count += 1
#             if won_battles_count % 3 == 0:
#                 energy += won_battles_count
#         else:
#             print(f'Not enough energy! Game ends with {won_battles_count} won battles and {energy} energy')
#             break


# # Task 2
#
# people = int(input())
#
# lift = list(map(int, input().split(' ')))
#
# while people and not all(x == 4 for x in lift):
#     for i in range(len(lift)):
#         if lift[i] < 4:
#             places = 4 - lift[i]
#             if places <= people:
#                 people -= places
#                 lift[i] = 4
#             else:
#                 lift[i] += people
#                 people = 0
#
# if people > 0 and all(x == 4 for x in lift):
#     print(f"There isn't enough space! {people} people in a queue!")
# elif people == 0 and not all(x == 4 for x in lift):
#     print(f"The lift has empty spots!")
#
# print(' '.join(list(map(str, lift))))


# Task 3

numbers = list(map(int, input().split(' ')))
average = sum(numbers) / len(numbers)
above_average = [n for n in numbers if n > average]

if not above_average:
    print('No')
else:
    result = sorted(above_average, key=lambda x: -x)[: 5]
    print(' '.join(list(map(str, result))))


















