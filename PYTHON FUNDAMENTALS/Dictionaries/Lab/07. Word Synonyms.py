pairs_count = int(input())
synonym_dict = {}

for command in range(0, pairs_count):
    key = input()
    value = input()
    if key not in synonym_dict:
        synonym_dict[key] = [value]
    else:
        synonym_dict[key].append(value)

for key, value in synonym_dict.items():
    print(f"{key} -", end=" ")
    print(f"{', '.join(value)}")




