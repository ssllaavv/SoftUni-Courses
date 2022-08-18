input_line = input().split()

number = 0
current_result = 0
result = 0

for string in input_line:
    el = string.strip()
    first_letter = el[0]
    last_letter = el[-1]
    number = int(el[1:-1:1])
    if first_letter.isupper():
        current_result = number / (ord(first_letter) - 64)
    else:
        current_result = number * (ord(first_letter) - 96)

    if last_letter.isupper():
        current_result -= (ord(last_letter) - 64)
    else:
        current_result += (ord(last_letter) - 96)
    result += current_result

print(f"{result:.2f}")
