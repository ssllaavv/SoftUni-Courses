import re

pattern = r'(>{2}(?P<Furniture>[a-zA-Z]+)<{2}(?P<Price>\d+(\.\d+)*)\!(?P<Quantity>\d+))'
current_purchase_amount = 0
total_amount = 0
result = ""
fur_list = []

purchase = input()
while purchase != "Purchase":
    result = re.finditer(pattern, purchase)
    for furniture in result:
        fur_dict = furniture.groupdict()
        fur_list.append(fur_dict['Furniture'])
        current_purchase_amount = float(fur_dict['Price']) * int(fur_dict['Quantity'])
        total_amount += current_purchase_amount

    purchase = input()
print("Bought furniture:")
for item in fur_list:
    print(item)
print(f"Total money spend: {total_amount:.2f}")

