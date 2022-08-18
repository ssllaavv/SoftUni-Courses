words = input().split()
even_words = [word for word in words if len(word) % 2 == 0]
for el in even_words:
    print(el)