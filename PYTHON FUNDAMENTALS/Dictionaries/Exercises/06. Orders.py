products_dict = {}

while True:
    input_line = input().split()
    if input_line[0] == "buy":
        break
    if input_line[0] not in products_dict:
        products_dict[input_line[0]] = [float(input_line[1]), int(input_line[2])]
    else:
        products_dict[input_line[0]][0] = float(input_line[1])
        products_dict[input_line[0]][1] += int(input_line[2])
total_price = 0
for key, value in products_dict.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")

