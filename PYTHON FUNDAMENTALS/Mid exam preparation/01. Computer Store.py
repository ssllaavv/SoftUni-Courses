price_factor = 1
bill = 0
while True:
    command = input()
    if command == "special":
        price_factor = 0.9
        break
    elif command == "regular":
        break
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
    else:
        bill += current_price
if bill == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!"
          f"\nPrice without taxes: {bill:.2f}$"
          f"\nTaxes: {(.2 * bill):.2f}$"
          f"\n-----------"
          f"\nTotal price: {(bill * 1.2 * price_factor):.2f}$")
