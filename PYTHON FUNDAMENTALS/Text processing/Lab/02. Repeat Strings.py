input_line = input().split()
result = ""
for el in input_line:
    result += el * len(el)
print(result)