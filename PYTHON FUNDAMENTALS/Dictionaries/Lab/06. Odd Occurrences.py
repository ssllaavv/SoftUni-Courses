words = input().split()
words_count_dict = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in words_count_dict:
        words_count_dict[word_lower] = 0
    words_count_dict[word_lower] += 1

for key, value in words_count_dict.items():
    if value % 2 != 0:
        print(key, end=" ")
