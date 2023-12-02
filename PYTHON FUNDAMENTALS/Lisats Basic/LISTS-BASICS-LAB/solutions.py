# # Task  1 - Strange Zoo
#
# tail = input()
# body = input()
# head = input()
#
# meerkat = [tail, body, head]
#
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
#
# print(meerkat)


# # Task 2 - Courses
#
# n = int(input())
#
# courses = []
#
# for i in range(n):
#     courses.append(input())
#
# print(courses)


# # Task 3 - List Statistics
# n = int(input())
#
# positives = []
# negatives = []
#
# for i in range(n):
#     num = int(input())
#     if num >= 0:
#         positives.append(num)
#     else:
#         negatives.append(num)
#
# print(f"{positives}"
#       f"\n{negatives}"
#       f"\nCount of positives: {len(positives)}"
#       f"\nSum of negatives: {sum(negatives)}")


# # Task 4 - Search - first solution
#
# n = int(input())
# searched_word = input()
#
# list_of_all_sentences = []
# filtered_sentences = []
#
# for i in range(n):
#     sentence = input()
#     list_of_all_sentences.append(sentence)
#     if searched_word in sentence:
#         filtered_sentences.append(sentence)
#
# print(list_of_all_sentences)
# print(filtered_sentences)


# # Task 4 - Search - second solution
#
# n = int(input())
# searched_word = input()
#
# list_of_all_sentences = []
#
#
# for i in range(n):
#     sentence = input()
#     list_of_all_sentences.append(sentence)
#
# filtered_sentences = [s for s in list_of_all_sentences if searched_word in s]
#
# print(list_of_all_sentences)
# print(filtered_sentences)


# Task 5

n = int(input())

all_numbers = []
filtered_numbers = []

for i in range(n):
    all_numbers.append(int(input()))

command = input()

if command == 'even':
    for num in all_numbers:
        if num % 2 == 0:
            filtered_numbers.append(num)
elif command == 'odd':
    for num in all_numbers:
        if num % 2 == 1:
            filtered_numbers.append(num)
elif command == 'positive':
    for num in all_numbers:
        if num >= 0:
            filtered_numbers.append(num)
elif command == 'negative':
    for num in all_numbers:
        if num < 0:
            filtered_numbers.append(num)

print(filtered_numbers)















