products_dict = {}

while True:
    input_line = input().split(": ")
    if input_line[0] == "statistics":
        break
    if input_line[0] not in products_dict:
        products_dict[input_line[0]] = 0
    products_dict[input_line[0]] += int(input_line[1])

count_all_products = 0
sum_all_quantities = 0


print("Products in stock:")
for key, value in products_dict.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products_dict.keys())}")
print(f"Total Quantity: {sum(products_dict.values())}")
