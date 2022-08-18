text = (input()).upper() + " "
result = ""
current_text = ""
multiplier = 0

for char in text:
    if multiplier == 0:
        if not char.isdigit():
            current_text += char
        else:
            multiplier = int(char)
    else:
        if char.isdigit():
            multiplier = 10 * multiplier + int(char)
        result += multiplier * current_text
        multiplier = 0
        current_text = char

unique_chars = set(result)
print(f"Unique symbols used: {len(unique_chars)}")
print(result)


