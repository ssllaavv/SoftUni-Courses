names = input().split(", ")

is_valid = True
for name in names:
    is_valid = True
    if len(name) in range(3, 17):
        for l in name:
            if (l.isalnum() or l == "-" or l == "_") and l != " ":
                continue
            else:
                is_valid = False
                break
        if is_valid:
            print(name)

