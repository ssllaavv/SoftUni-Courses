heroes_count = int(input())

heroes = {}
for line in range(heroes_count):
    hero, hp, mp = input().split(" ")
    heroes[hero] = {}
    heroes[hero]["hp"] = int(hp)
    heroes[hero]["mp"] = int(mp)

input_line = input().split(" - ")

while input_line[0] != "End":
    command = input_line[0]
    hero_name = input_line[1]
    amount = int(input_line[2])
    if command == "CastSpell":
        spell = input_line[3]
        diff = heroes[hero_name]["mp"] - amount
        if diff >= 0:
            heroes[hero_name]["mp"] = diff
            print(f"{hero_name} has successfully cast {spell} and now has {diff} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell}!")
            diff = 0
    if command == "TakeDamage":
        attacker = input_line[3]
        diff = heroes[hero_name]["hp"] - amount
        if diff > 0:
            heroes[hero_name]["hp"] = diff
            print(f"{hero_name} was hit for {amount} HP by {attacker} and now has {diff} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
    if command == "Recharge":
        new_value = heroes[hero_name]["mp"] + amount
        if new_value > 200:
            actual_amount = amount - (new_value - 200)
            heroes[hero_name]["mp"] = 200
            print(f"{hero_name} recharged for {actual_amount} MP!")
        else:
            heroes[hero_name]["mp"] = new_value
            print(f"{hero_name} recharged for {amount} MP!")
    if command == "Heal":
        new_value = heroes[hero_name]["hp"] + amount
        if new_value > 100:
            actual_amount = amount - (new_value - 100)
            heroes[hero_name]["hp"] = 100
            print(f"{hero_name} healed for {actual_amount} HP!")
        else:
            heroes[hero_name]["hp"] = new_value
            print(f"{hero_name} healed for {amount} HP!")

    input_line = input().split(" - ")

for name, value in heroes.items():
    print(name)
    for k, v in value.items():
        print(f"  {k.upper()}: {v}")
