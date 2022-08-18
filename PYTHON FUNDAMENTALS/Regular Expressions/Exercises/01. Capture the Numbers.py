import re

pattern = r"\d+"
line_input = input()
result = []
while line_input:
    result += re.findall(pattern, line_input)
    line_input = input()
print(*result)

