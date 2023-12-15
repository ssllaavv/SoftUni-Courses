# # Task 1
#
# n = int(input())
#
# for i in range(n):
#     sentence = input()
#     name = ''
#     age = ''
#
#     name_started = False
#     name_ended = False
#     age_started = False
#     age_ended = False
#
#     for l in sentence:
#         if l == '@':
#             name_started = True
#         elif l == '|':
#             name_ended = True
#         elif l == '#':
#             age_started = True
#         elif l == '*':
#             age_ended = True
#         else:
#             if name_started and not name_ended:
#                 name += l
#             elif age_started and not age_ended:
#                 age += l
#
#     print(f'{name} is {age} years old.')


# # Task 2
#
# char_1 = ord(input())
# char_2 = ord(input())
#
# target_range = (min(char_1, char_2), max(char_1, char_2))
# sum_of_ascii_codes = 0
#
# sentence = input()
# for l in sentence:
#     if target_range[0] < ord(l) < target_range[1]:
#         sum_of_ascii_codes += ord(l)
#
# print(sum_of_ascii_codes)


# # Task 3
# from math import ceil
#
# numbers = list(map(int, input().split(' ')))
#
# while True:
#     sentence = input()
#     if sentence == 'find':
#         break
#
#     factor = len(sentence) / len(numbers)
#     more_numbers = numbers * ceil(factor)
#     more_numbers = more_numbers[:len(sentence)]
#
#     symbols_and_codes = tuple(zip(sentence, more_numbers))
#
#     decoded_sentence = [chr(ord(k) - v) for k, v in symbols_and_codes]
#
#     treasure_start = decoded_sentence.index('&')
#     treasure_end = decoded_sentence.index('&', treasure_start + 1)
#
#     coordinates_start = decoded_sentence.index('<')
#     coordinates_end = decoded_sentence.index('>')
#
#     treasure = ''.join(decoded_sentence[treasure_start + 1: treasure_end])
#     coordinates = ''.join(decoded_sentence[coordinates_start + 1: coordinates_end])
#
#     print(f'Found {treasure} at {coordinates}')



# # Task 4
#
# morse_dict = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
#     'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
#     'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#     'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
#     '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
#     '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
#     ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
#     '$': '...-..-', '@': '.--.-.', ' ': '/'
# }
#
# inverted_morse_dict = {v: k for k, v in morse_dict.items()}
#
# code = input().split(' | ')
# decoded_sentence = []
#
# for code_word in code:
#     word = ''
#     letters = code_word.strip().split(' ')
#     for l in letters:
#         word += inverted_morse_dict[l]
#
#     decoded_sentence.append(word)
#
# print(' '.join(decoded_sentence))


# Task 5

title = input()
content = input()
comments = []

while True:
    comment = input()
    if comment == 'end of comments':
        break

    comments.append(comment)

result = f'<h1>\n    {title}\n</h1>\n<article>\n    {content}\n</article>'
for comment in comments:
    result += f'\n<div>\n    {comment}\n</div>'

print(result)





































