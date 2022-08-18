energy = int(input())

won_battles = 0
energy_is_not_enough = False
input_line = input()

while input_line != "End of battle":
    distance = int(input_line)
    if distance <= energy:
        won_battles += 1
        if won_battles % 3 == 0:
            energy += won_battles
        energy -= distance
    else:
        energy_is_not_enough = 1
        break
    input_line = input()
if energy_is_not_enough:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
else:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
