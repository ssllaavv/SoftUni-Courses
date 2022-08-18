orders_count = int(input())

total_amount = 0.0
for order in range(orders_count):
    capsule_price = float(input())
    days = int(input())
    capsules_count = int(input())

    if capsule_price < 0.01 or capsule_price > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_count < 1 or capsules_count > 2000:
        continue

    order_amount = capsule_price * capsules_count * days
    print(f"The price for the coffee is: ${order_amount:.2f}")
    total_amount += order_amount
print(f"Total: ${total_amount:.2f}")
