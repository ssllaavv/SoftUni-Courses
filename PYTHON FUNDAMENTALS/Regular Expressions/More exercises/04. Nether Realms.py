import re

pattern_remove_space = r"\S.*\S"
pattern_for_health = r'[^0-9\+\-\*\/\.]'
pattern_damage = r'(?P<Number>[\+\-]*\d+(\.\d+)*)'
pattern_operator = r'[*|\\]{1}'

names = []
raw_names = input().split(",")
for el in raw_names:
    name = re.findall(pattern_remove_space, el)
    names += name
names.sort()

for name in names:
    health = 0
    damage = 0
    matches_health = re.findall(pattern_for_health, name)
    for letter in matches_health:
        health += int(ord(letter))
    matches_damage = re.finditer(pattern_damage, name)
    for match in matches_damage:
        number = match.group("Number")
        damage += float(number)
    matches_operator = re.findall(pattern_operator, name)
    for operator in matches_operator:
        if operator == '*':
            damage *= 2
        if operator == '/':
            damage /= 2
    print(f'{name} - {health} health, {damage:.2f} damage')
