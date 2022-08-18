import re

list_of_competitors = input().split(", ")
dict_of_competitors = {}

for competitor in list_of_competitors:
    dict_of_competitors[competitor] = 0

pattern_name = r'[A-Z]+[a-z]*'
pattern_score = r'\d'

while True:
    some_string = input()
    if some_string == "end of race":
        break
    name_as_list = re.findall(pattern_name, some_string)
    name = f'{"".join(name_as_list)}'
    score_as_list = re.findall(pattern_score, some_string)
    score = 0
    for number in score_as_list:
        score += int(number)

    if name in dict_of_competitors.keys():
        dict_of_competitors[name] += score
sorted_dict = dict(sorted(dict_of_competitors.items(), key=lambda item: item[1]))
key_list = list(sorted_dict)

print(f"1st place: {key_list[-1]}")
print(f"2nd place: {key_list[-2]}")
print(f"3rd place: {key_list[-3]}")