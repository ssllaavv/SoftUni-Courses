quantity = int(input())
days = int(input())

ornament_price = 2
skirt_price = 5
garland_price = 3
lights_price = 15

bill = 0
spirit = 0

for d in range(1, days +1):
    if d % 11 == 0:
        quantity += 2
    if d % 2 == 0:
        bill += quantity * ornament_price
        spirit += 5
    if d % 3 == 0:
        bill += quantity * (skirt_price + garland_price)
        spirit += 13
    if d % 5 == 0:
        bill += quantity * lights_price
        spirit += 17
    if d % 15 == 0:
        spirit += 30
    if d % 10 == 0:
        spirit -= 20
        bill += skirt_price + garland_price + lights_price


if days % 10 == 0:
    spirit -= 30

print(f"Total cost: {bill:.0f}")
print(f"Total spirit: {spirit}")

