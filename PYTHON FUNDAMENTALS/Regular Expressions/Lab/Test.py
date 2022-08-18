import re

text = "the rain in Spain"

pattern = r"ai"

print(*re.findall(pattern, text))
