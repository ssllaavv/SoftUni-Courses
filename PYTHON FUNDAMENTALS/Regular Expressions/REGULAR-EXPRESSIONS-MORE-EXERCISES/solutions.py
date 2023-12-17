# Task 1
import re

competitors = input().split(', ')
competitors_results = {}

while True:
    command = input()
    if command == 'end of race':
        break

    pattern_competitor = r'[A-Za-z]+'
    pattern_distance = r'\d+'

    competitor_list = re.findall(pattern_competitor, command)
    competitor = ''.join(competitor_list)
    if competitor in competitors:
        distances_string_list = re.findall(pattern_distance, command)
        distances_string = ''.join(distances_string_list)
        distance = sum(list(map(int, distances_string)))
        if competitor not in competitors_results:
            competitors_results[competitor] = 0
        competitors_results[competitor] += distance

sorted_competitors = tuple(sorted(competitors_results.items(), key=lambda x: -x[1]))

print(f'1st place: {sorted_competitors[0][0]}')
print(f'2nd place: {sorted_competitors[1][0]}')
print(f'3rd place: {sorted_competitors[2][0]}')



# Task 2
import re

total_income = 0

while True:
    line = input()
    if line == 'end of shift':
        break

    # pattern = r'%(?P<customer>[A-Z][a-z]+)%[^\|\$%\.<>]*' \
    #           r'<(?P<product>\w+)>[^\|\$%\.<>]*' \
    #           r'\|(?P<count>\d+)\|[^\|\$%\.<>\d]*' \
    #           r'(?P<price>([0]|[1-9][\d]*)(\.\d+)?)\$'

    pattern =  r'^%(?P<customer>[A-Z][a-z]+)%.*' \
               r'<(?P<product>[\w]+)>.*' \
               r'\|(?P<count>\d+)\|\D*' \
               r'(?P<price>\d+(\.\d+)*)\$$'

    matches = [m.groupdict() for m in re.finditer(pattern, line)]
    if matches:
        match = matches[0]
        amount = float(match['price']) * int(match['count'])
        total_income += amount
        print(f"{match['customer']}: {match['product']} - {amount:.2f}")

print(f'Total income: {total_income:.2f}')

# Task 3
import re

n = int(input())

attacked_planets = []
destroyed_planets = []

for _ in range(n):
    message = input()

    key = sum([1 for l in message.lower() if l in 'star'])
    decoded_message = ''.join([chr(ord(l) - key) for l in message])
    # print(decoded_message)

    pattern = r'@(?P<name>[A-z]+)[^@/-/!:>]*' \
              r':(?P<population>\d+)[^@/-/!:>]*' \
              r'!(?P<attack>[AD])![^@/-/!:>]*' \
              r'->(?P<soldiers>\d+)[^@/-/!:>]*'

    matches = [match.groupdict() for match in re.finditer(pattern, decoded_message)]

    if matches and matches[0]['attack'] == 'A':
        attacked_planets.append(matches[0])
    elif matches and matches[0]['attack'] == 'D':
        destroyed_planets.append(matches[0])


attacked_planets = list(sorted(attacked_planets, key=lambda x: x['name']))
destroyed_planets = list(sorted(destroyed_planets, key=lambda x: x['name']))

print(f'Attacked planets: {len(attacked_planets)}')
for p in attacked_planets:
    print(f'-> {p["name"]}')

print(f'Destroyed planets: {len(destroyed_planets)}')
for p in destroyed_planets:
    print(f'-> {p["name"]}')


# Task 4
import re


names = input().split(',')
names = [n.strip() for n in names]

demons_dict = {name: [0, 0] for name in names}

pattern_health = r"[^\+\-\*\/\.\d]"
# pattern_damage = r'\-*([0]|[1-9]\d*)(\.\d+)?'
pattern_damage = r"([\+\-]?[\d]+(\.\d+)?)"
pattern_factors = r"[\*\/]"

for name in names:
    health = sum([ord(letter) for letter in re.findall(pattern_health, name)])
    damage = sum([float(match[0]) for match in re.findall(pattern_damage, name)])
    factors = [2 if match == "*" else 0.5 for match in re.findall(pattern_factors, name)]
    for n in factors:
        damage *= n

    demons_dict[name] = [health, damage]

demons_dict = dict(sorted(demons_dict.items()))

for demon, specs in demons_dict.items():
    print(f'{demon} - {specs[0]} health, {specs[1]:.2f} damage')


# Task 5
import re

html = input()

pattern_raw = r'<title(?P<title>.*)/title>.*<body(?P<body>.*)/body>'
pattern_text = r'>(?P<text>[^<]+)<'
pattern_new_line = r'\\n'

raw_matches = [match.groupdict() for match in re.finditer(pattern_raw, html)]
raw_title = raw_matches[0]['title']
raw_body = raw_matches[0]['body']

title_text_matches = [match.groupdict() for match in re.finditer(pattern_text, raw_title)]
body_text_matches = [match.groupdict() for match in re.finditer(pattern_text, raw_body)]

title_text = ""
for m in title_text_matches:
    title_text += m['text'].strip() + " "

body_text = ""
for m in body_text_matches:
    body_text += m['text'].strip() + " "

title_text = re.sub(pattern_new_line, "", title_text)
body_text = re.sub(pattern_new_line, "", body_text)

print(f'Title: {title_text.strip()}')
print(f'Content: {body_text.strip()}')




































