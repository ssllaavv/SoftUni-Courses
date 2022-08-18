words = input().split()
even_words = list(filter(lambda word: len(word) % 2 == 0, words))
for el in even_words:
    print(el)
