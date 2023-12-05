# # Task 1
#
# strings = input().split(', ')
# words = input().split(', ')
#
# result = [s for s in strings if any(s in w for w in words)]
#
# print(result)


# # Task 2
#
# ver_list = input().split('.')
# new_ver_as_string = str(int(ver_list[0] + ver_list[1] + ver_list[2]) + 1)
# print('.'.join(list(new_ver_as_string)))


# # Task 3
#
# obj = (w for w in input().split(' ') if len(w) % 2 == 0)
#
# for el in obj:
#     print(el)


# # Task 4
#
# numbers = list(map(int, input().split(', ')))
#
# positives = [n for n in numbers if n >= 0]
# negatives = list(filter(lambda n: n < 0, numbers))
# odds = [n for n in numbers if n % 2 == 1]
# evens = list(filter(lambda n: n not in odds, numbers))
#
# print(f"Positive: {', '.join(list(map(str, positives)))}\n"
#       f"Negative: {', '.join(list(map(str, negatives)))}\n"
#       f"Even: {', '.join(list(map(str, evens)))}\n"
#       f"Odd: {', '.join(list(map(str, odds)))}")

# # Task 5
#
# rooms_count = int(input())
#
# total_free_chairs = 0
# enough_chairs = True
#
# for i in range(1, rooms_count + 1):
#
#     input_line = input().split(' ')
#
#     chairs = len(input_line[0])
#     guests = int(input_line[1])
#     free_chairs = chairs - guests
#
#     if free_chairs < 0:
#         print(f'{abs(free_chairs)} more chairs needed in room {i}')
#         enough_chairs = False
#
#     total_free_chairs += free_chairs
#
# if enough_chairs:
#     print(f'Game On, {total_free_chairs} free chairs left')


# # Task 6
#
# def represent_electron_shells(electrons: int):
#     number_of_electron = electrons
#     shells = []
#
#     n = 1
#     while number_of_electron > 0:
#         if 2 * n ** 2 >= number_of_electron:
#             shells.append(number_of_electron)
#             break
#         shells.append(2 * n ** 2)
#         number_of_electron -= 2 * n ** 2
#         n += 1
#
#     return shells
#
#
# print(represent_electron_shells(int(input())))


# # Task 7
#
# numbers = list(map(int, input().split(', ')))
#
# result = []
#
# i = 1
# while numbers:
#     group = []
#     for n in range(len(numbers) - 1, -1, -1):
#         if numbers[n] <= 10 * i:
#             group.append(numbers.pop(n))
#     result.append(list(reversed(group)))
#     i += 1
#
# for i in range(len(result)):
#     print(f"Group of {i + 1}0's: {result[i]}")


# # Task 8
#
# encoded_words = input().split(' ')
#
# deciphered_list = []
#
# for w in encoded_words:
#     number = [n for n in w if n.isdigit()]
#     first_letter = chr(int(''.join(number)))
#     letters = [l for l in w if l.isalpha()]
#     letters[0], letters[-1] = letters[-1], letters[0]
#     word = first_letter + ''.join(letters)
#     deciphered_list.append(word)
#
# print(' '.join(deciphered_list))


# Task 9

text = input().split(' ')

while True:
    input_line = input().split(' ')
    if input_line[0] == '3:1':
        break

    if input_line[0] == 'merge':
        start_index = int(input_line[1])
        end_index = int(input_line[2])

        if (0 <= start_index < len(text)) and (0 <= end_index < len(text)):
            left = text[: start_index]
            right = text[end_index + 1:]
            middle = ''.join(text[start_index: end_index + 1])
            text = left
            text.append(middle)
            text += right
        elif start_index < 0 and (0 <= end_index < len(text)):
            right = text[end_index + 1:]
            middle = ''.join(text[: end_index + 1])
            text.clear()
            text.append(middle)
            text += right
        elif (0 <= start_index < len(text)) and end_index >= len(text):
            left = text[: start_index]
            middle = ''.join(text[start_index:])
            text = left
            text.append(middle)

    elif input_line[0] == 'divide':
        index = int(input_line[1])
        partitions = int(input_line[2])

        word = list(text[index])

        size = len(word) // partitions

        divided_word = []

        for i in range(partitions):
            el = ''
            for _ in range(size):
                el += word.pop(0)
            divided_word.append(el)

        for el in word:
            divided_word[-1] += el

        text.pop(index)
        for i in range(len(divided_word)):
            text.insert(index + i, divided_word[i])

print(' '.join(text))



























