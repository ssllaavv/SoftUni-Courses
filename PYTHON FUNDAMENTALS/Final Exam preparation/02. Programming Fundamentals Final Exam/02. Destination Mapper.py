import re

text = input()
result = []

pattern = r"(?P<Suround>[=|/])(?P<Destination>[A-Z]{1}[A-Za-z]{2,})(?P=Suround)"

matches = re.finditer(pattern, text)
for match in matches:
    result.append(match.group("Destination"))

travel_points = 0
for el in result:
    travel_points += len(el)

print(f"Destinations: {', '.join(result)}")
print(f"Travel Points: {travel_points}")
