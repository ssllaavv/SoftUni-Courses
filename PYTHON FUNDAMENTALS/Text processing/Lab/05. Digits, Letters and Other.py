some_stings = input()

digits = ""
letters = ""
other_chars = ""

for char in some_stings:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        other_chars += char

print(digits)
print(letters)
print(other_chars)
