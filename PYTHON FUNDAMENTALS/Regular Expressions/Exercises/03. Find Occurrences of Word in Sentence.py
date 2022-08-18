import re

sentence = input()
word = input()
pattern = fr'\b{word}\b'

list_of_occurrence = re.findall(pattern, sentence, flags=re.I)

print(len(list_of_occurrence))
