import re

count = int(input())

pattern_validity = r"(@{1}#+)(?P<Barcode>[A-Z]{1}[A-Za-z\d]{4,}[A-Z]{1})(@{1}#+)"

pattern_prod_group = r"\d"

for i in range(count):
    barcode = input()
    result = ""
    matches = re.finditer(pattern_validity, barcode)
    for match in matches:
        result = match.group("Barcode")
    if len(result) > 0:
        digits = re.finditer(pattern_prod_group, result)
        prod_group = ""
        for digit in digits:
            prod_group += digit.group()
        if len(prod_group) > 0:
            print(f"Product group: {prod_group}")
            prod_group = ""
        else:
            print("Product group: 00")

    else:
        print("Invalid barcode")

