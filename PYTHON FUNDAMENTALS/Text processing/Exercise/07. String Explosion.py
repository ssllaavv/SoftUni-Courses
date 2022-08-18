text = input()

strength = 0
result = ""

for index in range(len(text)):
    if strength == 0:
        if text[index] != ">":
            result += text[index]
        else:
            strength = int(text[index + 1])
            result += ">"
    else:
        if text[index] != ">":
            strength -= 1
            continue
        else:
            strength += int(text[index + 1])
            result += ">"
print(result)


