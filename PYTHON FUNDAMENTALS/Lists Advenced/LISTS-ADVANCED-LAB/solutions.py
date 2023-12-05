# Task 1

def filter_no_vowels(sentence: str) -> str:
    vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
    result = [letter for letter in sentence if letter not in vowels]

    return ''.join(result)


sentence = input()

print(filter_no_vowels(sentence))


# Task 2

length = int(input())

train = [0] * length

while True:
    command_line = input().split(' ')
    if command_line[0] == 'End':
        break

    command = command_line[0]
    arg_2 = int(command_line[1])

    if command == 'insert':
        count = int(command_line[2])
        train[arg_2] += count
    elif command == 'leave':
        count = int(command_line[2])
        train[arg_2] -= count
    elif command == 'add':
        train[-1] += arg_2


print(train)


# Task 3

tasks_list = [0] * 10

result = []

while True:
    command = input()
    if command == 'End':
        break

    priority_and_task = command.split('-')
    priority = int(priority_and_task[0])
    task = priority_and_task[1]

    tasks_list.pop(priority - 1)
    tasks_list.insert(priority - 1, task)

    result = [t for t in tasks_list if t != 0]

print(result)


# Task 4

words = input().split(' ')
searched_palindrome = input()

palindromes = [''.join(list(reversed(w))) for w in words if ''.join(list(reversed(w))) == w]
count_of_occurrence = palindromes.count(searched_palindrome)

print(palindromes)
print(f'Found palindrome {count_of_occurrence} times')


# Task 5

names = input().split(', ')

sorted_name = sorted(names, key=lambda x: (-len(x), x), reverse=False)

print(sorted_name)


# Task 6

input_line = input()
numbers = list(map(int, input_line.split(', ')))
indexes = list(filter(lambda x: numbers[x] % 2 == 0, range(len(numbers))))

print(indexes)


# Task 7

employees_happiness = list(map(int, input().split(' ')))
factor = int(input())

employees_happiness = [h * factor for h in employees_happiness]

average_happiness = sum(employees_happiness) / len(employees_happiness)

happy_count = len([e for e in employees_happiness if e >= average_happiness])

unhappy_count = len(employees_happiness) - happy_count

if happy_count >= unhappy_count:
    print(f'Score: {happy_count}/{len(employees_happiness)}. Employees are happy!')
else:
    print(f'Score: {happy_count}/{len(employees_happiness)}. Employees are not happy!')























