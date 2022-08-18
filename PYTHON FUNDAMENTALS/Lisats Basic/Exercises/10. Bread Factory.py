events_list = input().split("|")
energy = 100
money = 100

is_closed = False

for element in events_list:
    event = element.split("-")
    if event[0] == "rest":
        if energy + int(event[1]) > 100:
            gained_energy = 100 - energy
            energy = 100
        else:
            gained_energy = int(event[1])
            energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event[0] == "order":
        if energy >= 30:
            energy -= 30
            money += int(event[1])
            print(f"You earned {int(event[1])} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if int(event[1]) <= money:
            money -= int(event[1])
            print(f"You bought {event[0]}.")
        else:
            print(f"Closed! Cannot afford {event[0]}.")
            is_closed = True
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {money}")
    print(f"Energy: {energy}")
