budget = float(input())
flour_price_kg = float(input())

eggs_price = .75 * flour_price_kg
milk_price = .25 * 1.25 * flour_price_kg

loaves_price = eggs_price + flour_price_kg + milk_price

painted_eggs_count = 0
loaves_count = 0

while budget >= loaves_price:
    loaves_count += 1
    painted_eggs_count += 3
    if loaves_count % 3 == 0:
        painted_eggs_count -= loaves_count - 2
    budget -= loaves_price


print(f"You made {loaves_count} loaves of Easter bread! Now you have {painted_eggs_count} eggs and {budget:.2f}BGN left.")
