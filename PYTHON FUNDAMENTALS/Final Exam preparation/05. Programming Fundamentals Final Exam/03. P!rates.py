town_dict = {}

while True:
    input_town = input().split("||")
    if input_town[0] == "Sail":
        break
    town = input_town[0]
    population = int(input_town[1])
    gold = int(input_town[2])
    if town not in town_dict.keys():
        town_dict[town] = [population, gold]
    else:
        town_dict[town][0] += population
        town_dict[town][1] += gold
while True:
    input_action = input().split("=>")
    if input_action[0] == "End":
        break
    if input_action[0] == "Plunder":
        town = input_action[1]
        population = int(input_action[2])
        gold = int(input_action[3])
        print(f"{town} plundered! {gold} gold stolen, {population} citizens killed.")
        town_dict[town][0] -= population
        town_dict[town][1] -= gold
        if (town_dict[town][0] == 0) or (town_dict[town][1] == 0):
            town_dict.pop(town)
            print(f"{town} has been wiped off the map!")

    if input_action[0] == "Prosper":
        town = input_action[1]
        gold = int(input_action[2])
        if gold <= 0:
            print("Gold added cannot be a negative number!")
        else:
            town_dict[town][1] += gold
            total_gold = town_dict[town][1]
            print(f"{gold} gold added to the city treasury. {town} now has {total_gold} gold.")
"""  
is_population = False
count = 0
for value in town_dict.values():
    if value[0] > 0:
        count += 1
if count > 0:
    print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")
    for town, value in town_dict.items():
        population = value[0]
        gold = value[1]
        if population > 0:
            print(f"{town} -> Population: {population} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
"""

if len(town_dict) >0:
    print(f"Ahoy, Captain! There are {len(town_dict)} wealthy settlements to go to:")
    for town, value in town_dict.items():
        population = value[0]
        gold = value[1]
        print(f"{town} -> Population: {population} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")