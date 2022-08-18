collection_of_items = input().split("|")
budget = float(input())

bought_items = []
profit = 0

for item in collection_of_items:
    current_item = item.split("->")
    if current_item[0] == "Clothes":
        if float(current_item[1]) <= 50:
            if budget >= float(current_item[1]):
                budget -= float(current_item[1])
                bought_items.append(f"{(1.4 * float(current_item[1])):.2f}")
                profit += .4 * float(current_item[1])
    elif current_item[0] == "Shoes":
        if float(current_item[1]) <= 35:
            if budget >= float(current_item[1]):
                budget -= float(current_item[1])
                bought_items.append(f"{(1.4 * float(current_item[1])):.2f}")
                profit += .4 * float(current_item[1])
    elif current_item[0] == "Accessories":
        if float(current_item[1]) <= 20.50:
            if budget >= float(current_item[1]):
                budget -= float(current_item[1])
                bought_items.append(f"{(1.4 * float(current_item[1])):.2f}")
                profit += .4 * float(current_item[1])

total_money = budget + profit + (profit * 2.5)
print(*bought_items)
print(f"Profit: {profit:.2f}")
if total_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
