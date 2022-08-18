import re
number_of_lines = int(input())
attacked_planets = []
destroyed_planets = []

for line in range(number_of_lines):
    line_input = input()
    to_subtract = 0
    decoded_line = ""
    chars = ["s", "t", "a", "r"]
    for char in chars:
        for c in line_input.lower():
            if c == char:
                to_subtract += 1
    for symbol in line_input:
        decoded_line += chr(ord(symbol) - to_subtract)

    pattern = r'@(?P<Planet>[A-Za-z]+)[^@\-!:>]*:(?P<Population>\d+)[^@\-!:>]*!(?P<State>[A|D]{1})![^@\-!:>]*\->(?P<Soldiers>\d+)'
    result = re.finditer(pattern, decoded_line)

    if result:
        for match in result:
            if match.group("State") == "A":
                attacked_planets.append(match.group("Planet"))
            if match.group("State") == "D":
                destroyed_planets.append(match.group("Planet"))

attacked_planets.sort()
destroyed_planets.sort()

print(f"Attacked planets: {len(attacked_planets)}")

for planet in attacked_planets:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in destroyed_planets:
    print(f"-> {planet}")
