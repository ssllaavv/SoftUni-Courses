import re

text = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
valid_nums = re.finditer(pattern, text)
numbers = ""
for num in valid_nums:
    numbers += f"{num.group()} "

print(numbers)