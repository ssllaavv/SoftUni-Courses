import re

pattern = r"\b[P<=_]([A-Za-z]+\b)"
text = input()
matches = re.findall(pattern, text)
print(','.join(matches))