# Task 1

strings = input().split(', ')
words = input().split(', ')

result = [s for s in strings if any(s in w for w in words)]

print(result)


# Task 2

ver_list = input().split('.')
new_ver_as_string = str(int(ver_list[0] + ver_list[1] + ver_list[2]) + 1)
print('.'.join(list(new_ver_as_string)))


# Task 3

obj = (w for w in input().split(' ') if len(w) % 2 == 0)

for el in obj:
    print(el)


# Task 4

numbers = list(map(int, input().split(', ')))

positives = [n for n in numbers if n >= 0]
negatives = list(filter(lambda n: n < 0, numbers))
odds = [n for n in numbers if n % 2 == 1]
evens = list(filter(lambda n: n not in odds, numbers))

print(f"Positive: {', '.join(list(map(str, positives)))}\n"
      f"Negative: {', '.join(list(map(str, negatives)))}\n"
      f"Even: {', '.join(list(map(str, evens)))}\n"
      f"Odd: {', '.join(list(map(str, odds)))}")

# Task 5

rooms_count = int(input())

total_free_chairs = 0
enough_chairs = True

for i in range(1, rooms_count + 1):

    input_line = input().split(' ')

    chairs = len(input_line[0])
    guests = int(input_line[1])
    free_chairs = chairs - guests

    if free_chairs < 0:
        print(f'{abs(free_chairs)} more chairs needed in room {i}')
        enough_chairs = False

    total_free_chairs += free_chairs

if enough_chairs:
    print(f'Game On, {total_free_chairs} free chairs left')


# Task 6

def represent_electron_shells(electrons: int):
    number_of_electron = electrons
    shells = []

    n = 1
    while number_of_electron > 0:
        if 2 * n ** 2 >= number_of_electron:
            shells.append(number_of_electron)
            break
        shells.append(2 * n ** 2)
        number_of_electron -= 2 * n ** 2
        n += 1

    return shells


print(represent_electron_shells(int(input())))


# Task 7

numbers = list(map(int, input().split(', ')))

result = []

i = 1
while numbers:
    group = []
    for n in range(len(numbers) - 1, -1, -1):
        if numbers[n] <= 10 * i:
            group.append(numbers.pop(n))
    result.append(list(reversed(group)))
    i += 1

for i in range(len(result)):
    print(f"Group of {i + 1}0's: {result[i]}")


# Task 8

encoded_words = input().split(' ')

deciphered_list = []

for w in encoded_words:
    number = [n for n in w if n.isdigit()]
    first_letter = chr(int(''.join(number)))
    letters = [l for l in w if l.isalpha()]
    letters[0], letters[-1] = letters[-1], letters[0]
    word = first_letter + ''.join(letters)
    deciphered_list.append(word)

print(' '.join(deciphered_list))


# Task 9

# read the input array
text = input().split(' ')


# separate merge logic in a function
def merge(array, start_ind, end_ind):
    left = array[: start_ind]
    right = array[end_ind + 1:]
    middle = ''.join(array[start_ind: end_ind + 1])
    result = left
    result.append(middle)
    result += right

    return result


# separate divide logic in a function
def divide(array, ind, parts):
    word = list(array[ind])
    size = len(word) // parts
    divided_word = []

    for i in range(parts):
        el = ''
        for _ in range(size):
            el += word.pop(0)
        divided_word.append(el)

    for el in word:
        divided_word[-1] += el

    array.pop(ind)
    for i in range(len(divided_word)):
        array.insert(ind + i, divided_word[i])

    return array


# start reading commands
while True:
    input_line = input().split(' ')
    if input_line[0] == '3:1':  # define break condition
        break

    # handel merge case
    if input_line[0] == 'merge':
        start_index = int(input_line[1])
        end_index = int(input_line[2])
        start_index = max(0, start_index)
        end_index = min(len(text), end_index)
        text = merge(text, start_index, end_index)

    # handel divide command
    elif input_line[0] == 'divide':
        index = int(input_line[1])
        partitions = int(input_line[2])
        text = divide(text, index, partitions)

# print final state of the array
print(' '.join(text))


# Task 10

# read the initial sequence
pokemons = list(map(int, input().split(' ')))

# assign variable for the output
result = 0


while pokemons:

    index = int(input())

    if 0 <= index < len(pokemons):
        value = pokemons.pop(index)
    else:
        if index < 0:
            value = pokemons.pop(0)
            pokemons.insert(0, pokemons[-1])
        else:
            value = pokemons.pop(-1)
            pokemons.append(pokemons[0])

    result += value
    for i in range(len(pokemons)):
        if pokemons[i] <= value:
            pokemons[i] += value
        else:
            pokemons[i] -= value

# print the result
print(result)


# Task 11

# read the initial sequence
lessons = input().split(', ')

# read commands until 'course start' is received
while True:
    command = input().split(':')
    if command[0] == 'course start':
        break

    # handle 'add' command
    if command[0] == 'Add':
        lesson = command[1]
        if lesson not in lessons:
            lessons.append(lesson)

    # handle 'insert' command
    elif command[0] == 'Insert':
        lesson = command[1]
        index = int(command[2])
        if lesson not in lessons:
            lessons.insert(index, lesson)

    # handle 'remove' command
    elif command[0] == 'Remove':
        lesson = command[1]
        if lesson in lessons:
            lessons.remove(lesson)
            if f'{lesson}-Exercise' in lessons:
                lessons.remove(f'{lesson}-Exercise')

    # handle 'swap' command
    elif command[0] == 'Swap':

        lesson_1 = command[1]
        lesson_2 = command[2]

        # check if both lessons exists
        if lesson_1 in lessons and lesson_2 in lessons:

            index_1 = lessons.index(lesson_1)
            index_2 = lessons.index(lesson_2)

            # swap the lessons
            lessons[index_1], lessons[index_2] = lessons[index_2], lessons[index_1]

            # if there are exercise it is removed prom its current place
            # After that it is inserted after related lesson
            if f'{lesson_1}-Exercise' in lessons:
                lessons.remove(f'{lesson_1}-Exercise')
                ind = lessons.index(lesson_1)
                lessons.insert(ind + 1, f'{lesson_1}-Exercise')

            elif f'{lesson_2}-Exercise' in lessons:
                lessons.remove(f'{lesson_2}-Exercise')
                ind = lessons.index(lesson_2)
                lessons.insert(ind + 1, f'{lesson_2}-Exercise')

    # handle exercise command
    elif command[0] == 'Exercise':
        lesson = command[1]
        if lesson in lessons:
            if f'{lesson}-Exercise' not in lessons:
                index = lessons.index(lesson)
                lessons.insert(index + 1, f'{lesson}-Exercise')
        else:
            lessons += [lesson, f'{lesson}-Exercise']

# print the output
for n, l in enumerate(lessons, 1):
    print(f'{n}.{l}')

