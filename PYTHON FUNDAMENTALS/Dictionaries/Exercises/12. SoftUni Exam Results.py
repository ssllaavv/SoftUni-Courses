languages_dict = {}
while True:
    input_line = input()
    if input_line == "exam finished":
        break
    input_token = input_line.split("-")
    if input_token[1] == "banned":
        for result_key, result_value in languages_dict.items():
            for key in result_value.keys():
                if input_token[0] == key:
                    languages_dict[result_key][key] += [input_token[1]]
        continue
    name, language, points = input_token

    if language not in languages_dict.keys():
        languages_dict[language] = {name: [points]}

    elif language in languages_dict.keys():
        for key, value in languages_dict.items():
            if (name in value.keys()) and (language == key):
               # if (languages_dict[language][name] != "banned") and int(languages_dict[language][name]) < int(points):
                languages_dict[language][name] += [points]
            elif (name not in value.keys()) and (language == key):
                languages_dict[language][name] = [points]
#print(languages_dict)
print("Results:")

for language, value in languages_dict.items():
    for student, score in value.items():
        if "banned" not in score:
            print(f"{student} | {max(score)}")
print("Submissions:")

submissions = 0

for k, v in languages_dict.items():
    for stud, scr in v.items():
        if "banned" in scr:
            submissions += len(scr) - 1
        else:
            submissions += len(scr)
    print(f"{k} - {submissions}")
    submissions = 0
