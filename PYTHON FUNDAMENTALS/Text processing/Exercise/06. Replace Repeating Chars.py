text = input()
result = ""
previous_letter = ""

for letter in text:
    if letter == previous_letter:
        pass
    else:
        previous_letter = letter
        result += letter
print(result)









