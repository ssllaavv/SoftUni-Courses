# Task 1

numbers = input().split()
reversed_numbers = []
while numbers:
    reversed_numbers.append(numbers.pop())
print(' '.join(reversed_numbers))


# Task 2

n = int(input())

stack = []

for _ in range(n):
    command = list(map(int, input().split()))
    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        if stack:
            stack.pop()
    elif command[0] == 3 and stack:
        print(max(stack))
    elif command[0] == 4 and stack:
        print(min(stack))


for i in range(len(stack) - 1, -1, -1):
    if i == 0:
        print(stack.pop())
    else:
        print(stack.pop(), end=", ")


# Task 3

from collections import deque

food = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders and food > 0:
    if food >= orders[0]:
        food -= orders.popleft()
    else:
        print(f'Orders left: {" ".join(list(map(str, orders)))}')
        break

if not orders:
    print('Orders complete')


# Task 4

delivery = list(map(int, input().split()))
capacity = int(input())

current_rack_capacity = 0
racks = 0

while delivery:
    if current_rack_capacity < delivery[-1]:
        racks += 1
        current_rack_capacity = capacity
    current_rack_capacity -= delivery.pop()

print(racks)


# Task 5
from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    pump = [int(x) for x in input().split()]
    pumps.append(pump)

for attempt in range(n):
    tank = 0
    failed = False

    for fuel, distance in pumps:
        tank += fuel
        if distance > tank:
            failed = True
            break
        else:
            tank -= distance
    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break



# Task 6

from collections import deque
sequence = deque(input())
opening_parenthesis = []

while sequence:
    if sequence[0] in ('{', '[', '('):
        opening_parenthesis.append(sequence.popleft())
    else:
        responding = None
        if sequence[0] == '}':
            responding = '{'
        elif sequence[0] == ']':
            responding = '['
        elif sequence[0] == ')':
            responding = '('

        if opening_parenthesis and opening_parenthesis[-1] == responding:
            opening_parenthesis.pop()
            sequence.popleft()
        else:
            print('NO')
            break

if not sequence and not opening_parenthesis:
    print('YES')



# # Task 7
# from collections import deque
#
# robots_tokens = input().split(';')
# robots = [(r.split('-')[0], int(r.split('-')[1])) for r in robots_tokens]
#
# busy_robots = []
#
# time_token = input().split(':')
# time_seconds = int(time_token[0]) * 60 * 60 + int(time_token[1]) * 60 + int(time_token[2])
#
# details_queue = deque()
#
# more_new_parts = True
#
# while True:
#     if more_new_parts:
#         detail = input()
#         if detail == 'End':
#             more_new_parts = False
#             continue
#     else:
#         if details_queue:
#             detail = details_queue.popleft()
#         else:
#             break
#
#     time_seconds += 1
#     for i in range(len(busy_robots) - 1, -1, - 1):
#         if busy_robots[i][1] > 1:
#             busy_robots[i][1] -= 1
#         else:
#             busy_robots.pop(i)
#
#     part_is_taken = False
#     for robot, time in robots:
#         if robot not in [r[0] for r in busy_robots]:
#             busy_robots.append([robot, time])
#             hours = time_seconds // 3600
#             hours = hours % 12
#             if hours < 10:
#                 hours = '0' + str(hours)
#             reminder = time_seconds % 3600
#             minutes = reminder // 60
#             if minutes < 10:
#                 minutes = '0' + str(minutes)
#             seconds = reminder % 60
#             if seconds < 10:
#                 seconds = '0' + str(seconds)
#
#             print(f'{robot} - {detail} [{hours}:{minutes}:{seconds}]')
#             part_is_taken = True
#             break
#     if not part_is_taken:
#         details_queue.append(detail)


# Task 7 - 2

from collections import deque


def convert_sec_to_time(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)


input_line = input().split(";")

robots_speeds_dict = {}
robot_end_times_dict = {}
time_in_seconds = 0
products_queue = deque()

hours, minutes, seconds = [int(x) for x in input().split(":")]
time_in_seconds = seconds + (60 * minutes) + (60 * 60 * hours)

for el in input_line:
    robot, time = el.split("-")
    robots_speeds_dict[robot] = int(time)
    robot_end_times_dict[robot] = time_in_seconds

while True:
    product = input()
    if product == "End":
        break
    products_queue.append(product)

while products_queue:
    time_in_seconds += 1

    for robot, time in robot_end_times_dict.items():

        if time <= time_in_seconds:
            robot_end_times_dict[robot] = time_in_seconds + robots_speeds_dict[robot]
            print(f"{robot} - {products_queue.popleft()} [{convert_sec_to_time(time_in_seconds)}]")
            break
    else:
        products_queue.append(products_queue.popleft())


# # Task 7 - 3
# from collections import deque
#
#
# def convert_clock_time_to_seconds(clock_time):
#     time_token = list(map(int, clock_time.split(':')))
#     return time_token[0] * 3600 + time_token[1] * 60 + time_token[2]
#
#
# def convert_seconds_to_cloc_time(time_seconds):
#     minutes, seconds = divmod(time_seconds, 60)
#     hours, minutes = divmod(minutes, 60)
#     return f'{hours:02}:{minutes:02}:{seconds:02}'
#
#
# robots_token = input().split(';')
# robots_dict = {r.split('-')[0]: int(r.split('-')[1]) for r in robots_token}
# products_queue = deque()
#
# time_in_seconds = convert_clock_time_to_seconds(input())
# robots_times = {r: time_in_seconds for r in robots_dict.keys()}
#
# while True:
#     product = input()
#     if product == 'End':
#         break
#     products_queue.append(product)
#
# while products_queue:
#     time_in_seconds += 1
#
#     for robot in robots_times.keys():
#         if robots_times[robot] <= time_in_seconds:
#             robots_times[robot] = time_in_seconds + robots_dict[robot]
#             print(f'{robot} - {products_queue.popleft()} [{convert_seconds_to_cloc_time(time_in_seconds)}]')
#             break
#     else:
#         products_queue.append(products_queue.popleft())
#


#
# # Task 8
# from collections import deque
#
# green_duration = int(input())
# free_window = int(input())
#
# cars_queue = deque()
# time_counter = 0
#
# cars_passed_counter = 0
# crash_happen = False
#
# while True:
#     command = input()
#     if command == 'END' or crash_happen:
#         break
#
#     if command == 'green':
#         time_counter = 0
#
#         while cars_queue and not crash_happen and time_counter < green_duration:
#             current_car = cars_queue.popleft()
#             cars_passed_counter += 1
#             current_car_symbols = deque(list(current_car))
#             current_symbol = ''
#             while time_counter < green_duration and current_car_symbols:
#                 current_symbol = current_car_symbols.popleft()
#                 time_counter += 1
#             if time_counter == green_duration:
#                 while current_car_symbols and time_counter < green_duration + free_window:
#                     time_counter += 1
#                     current_symbol = current_car_symbols.popleft()
#                 if current_car_symbols:
#                     crash_happen = True
#                     print(f'A crash happened!'
#                           f'\n{current_car} was hit at {current_car_symbols.popleft()}.')
#     else:
#         cars_queue.append(command)
#
# if not crash_happen:
#     print(f'Everyone is safe.\n'
#           f'{cars_passed_counter} total cars passed the crossroads.')


# # Task 9
# from collections import deque
#
# bullet_price = int(input())
# barrel_size = int(input())
# bullets = list(map(int, input().split()))
# locks = deque(list(map(int, input().split())))
# reward = int(input())
#
# bullets_counter = 0
#
# while locks and bullets:
#     bullets_counter += 1
#     bullet = bullets.pop()
#     if bullet <= locks[0]:
#         locks.popleft()
#         print('Bang!')
#     else:
#         print('Ping!')
#     if bullets_counter % barrel_size == 0 and bullets:
#         print('Reloading!')
#
# if not locks:
#     expenses = bullets_counter * bullet_price
#     profit = reward - expenses
#     print(f'{len(bullets)} bullets left. Earned ${profit}')
# else:
#     print(f"Couldn't get through. Locks left: {len(locks)}")


# Task 10
from collections import deque

cups = deque(list(map(int, input().split())))
bottles = list(map(int, input().split()))

wasted_water = 0

while cups and bottles:
    bottle = bottles.pop()
    if bottle >= cups[0]:
        wasted_water += bottle - cups.popleft()
    else:
        cups[0] -= bottle

if not cups:
    print(f'Bottles: {" ".join(list(map(str, bottles)))}')
elif not bottles:
    print(f'Cups: {" ".join(list(map(str, cups)))}')
print(f'Wasted litters of water: {wasted_water}')


