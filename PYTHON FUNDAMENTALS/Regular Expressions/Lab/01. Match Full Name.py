import re

text = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

print(*re.findall(pattern, text))
