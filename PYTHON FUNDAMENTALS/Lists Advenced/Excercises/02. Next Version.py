soft_ver = (input().split("."))
soft_ver_list = []

for el in soft_ver:
    soft_ver_list.append(int(el))

result = soft_ver_list.copy()

if soft_ver_list[2] == 9:
    if result[1] == 9:
        result[0] += 1
        result[1] = 0
        result[2] = 0
    else:
        result[1] += 1
        result[2] = 0
else:
    result[2] += 1

print(*result, sep=".")
