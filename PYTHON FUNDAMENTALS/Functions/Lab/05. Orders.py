def bill_calculator(prod, qtt):
    if prod == "coffee":
        return 1.5 * qtt
    elif prod == "water":
        return qtt
    elif prod == "coke":
        return 1.4 * qtt
    elif prod == "snacks":
        return 2 * qtt

product = input()
quantity = int(input())

print(f"{bill_calculator(product, quantity):.2f}")
