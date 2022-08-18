list_of_words = input().split(", ")

sorted_list = sorted(list_of_words, key=lambda x: (-len(x), x))

print(sorted_list)
