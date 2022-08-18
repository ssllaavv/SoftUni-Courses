import re

pattern = r'^%(?P<Customer>[A-Z][a-z]+)%.*<(?P<Product>[\w]+)>.*\|(?P<Count>\d+)\|\D*(?P<Price>\d+(\.\d+)*)\$$'
text = input()
total_amount = 0
while text != "end of shift":
    result = re.finditer(pattern, text)
    for match in result:
        amount = (int(match.group('Count'))*float(match.group('Price')))
        print(f"{match.group('Customer')}: {match.group('Product')} - {amount:.2f}")
        total_amount += amount

    text = input()
print(F'Total income: {total_amount:.2f}')