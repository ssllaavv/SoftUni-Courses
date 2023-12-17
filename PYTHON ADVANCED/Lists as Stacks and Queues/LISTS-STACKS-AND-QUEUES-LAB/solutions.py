# Task 1

text = list(input())
reversed_text = []
while text:
    reversed_text.append(text.pop())

print(''.join(reversed_text))


# Task 2

expression = list(input())
opening_parentheses = []

for i in range(len(expression)):
    if expression[i] == '(':
        opening_parentheses.append(i)
    elif expression[i] == ')':
        start_index = opening_parentheses.pop()
        end_index = i
        print(''.join(expression[start_index: end_index + 1]))


# Task 3

from collections import deque

queue = deque()

while True:
    command = input()
    if command == 'End':
        break
    if command == 'Paid':
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)

print(f'{len(queue)} people remaining.')


# Task 4

from collections import deque
queue = deque()

liters = int(input())

while True:
    command = input()
    if command == 'Start':
        break
    queue.append(command)

while True:
    command = input().split(' ')
    if command[0] == 'End':
        print(f'{liters} liters left')
        break

    if len(command) == 1:
        amount = int(command[0])
        if liters >= amount:
            liters -= amount
            print(f'{queue.popleft()} got water')
        else:
            print(f'{queue.popleft()} must wait')

    else:
        if command[0] == 'refill':
            amount = int(command[1])
            liters += amount


# Task 5

from collections import deque

names = input().split(' ')
n = int(input())
queue = deque(names)

counter = 1
while True:
    if counter == n:
        if len(queue) > 1:
            print(f'Removed {queue.popleft()}')
            counter = 1
        else:
            print(f'Last is {queue.popleft()}')
            break
    else:
        queue.append(queue.popleft())
        counter += 1


