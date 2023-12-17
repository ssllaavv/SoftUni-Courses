number_of_plants = int(input())

plants = {}

for pl in range(number_of_plants):
    plant, rarity = input().split("<->")
    plants[plant] = {}
    plants[plant]["rarity"] = int(rarity)
    plants[plant]["rating"] = []


while True:
    input_line = input().split(": ")
    command = input_line[0]
    if command == "Exhibition":
        break

    sub_command = (input_line[1]).split(" - ")
    plant = sub_command[0]

    if plant not in plants.keys():
        print("error")
    else:

        if command == "Rate":
            rating = int(sub_command[1])
            plants[plant]["rating"].append(rating)

        if command == "Update":
            new_rarity = int(sub_command[1])
            plants[plant]["rarity"] = new_rarity

        if command == "Reset":
            plants[plant]["rating"].clear()


print("Plants for the exhibition:")
for k, v in plants.items():
    if len(v["rating"]) > 0:
        average_rating = sum(v['rating']) / len(v['rating'])
    else:
        average_rating = 0.0
    print(f"- {k}; Rarity: {v['rarity']}; Rating: {average_rating:.2f}")

