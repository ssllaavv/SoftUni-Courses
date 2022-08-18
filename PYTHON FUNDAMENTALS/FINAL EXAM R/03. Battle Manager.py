warriors = {}

while True:
    input_line = input().split(":")
    command = input_line[0]
    if command == "Results":
        break

    if command == "Add":
        warrior = input_line[1]
        health = int(input_line[2])
        energy = int(input_line[3])
        if warrior not in warriors.keys():
            warriors[warrior] = {}
            warriors[warrior]["health"] = health
            warriors[warrior]["energy"] = energy

        else:
            warriors[warrior]["health"] += health

    if command == "Attack":
        attacker = input_line[1]
        defender = input_line[2]
        damage = int(input_line[3])

        if (attacker in warriors.keys()) and (defender in warriors.keys()):
            warriors[defender]["health"] -= damage
            warriors[attacker]["energy"] -= 1

            if warriors[defender]["health"] <= 0:
                del warriors[defender]
                print(f"{defender} was disqualified!")

            if warriors[attacker]["energy"] <= 0:
                del warriors[attacker]
                print(f"{attacker} was disqualified!")

    if command == "Delete":
        name = input_line[1]
        if name == "All":
            warriors.clear()
        else:
            if name in warriors.keys():
                del warriors[name]

print(f"People count: {len(warriors)}")
for warrior, values in warriors.items():
    print(f"{warrior} - {values['health']} - {values['energy']}")
