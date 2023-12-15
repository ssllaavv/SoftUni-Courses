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






































