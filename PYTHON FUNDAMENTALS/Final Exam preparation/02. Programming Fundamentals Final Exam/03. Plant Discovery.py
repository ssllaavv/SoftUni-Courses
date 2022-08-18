input_count = int(input())

plants = {}

for line in range(input_count):
    line_input = input().split("<->")
    plant, rarity = line_input[0], int(line_input[1])
    plants[plant] = {}
    plants[plant]["rarity"] = rarity
    plants[plant]["rating"] = []

while True:
    input_line = input().split(": ")
    command = input_line[0]
    if command == "Exhibition":
        break
    attributes = input_line[1].split(" - ")
    plant = attributes[0]
    if plant not in plants:
        print("error")
    else:
        if command == "Rate":
            rating = int(attributes[1])
            plants[plant]["rating"].append(rating)

        if command == "Update":
            new_rarity = int(attributes[1])
            plants[plant]["rarity"] = new_rarity

        if command == "Reset":
            plants[plant]["rating"] = []

for plant, value in plants.items():
    length = len(plants[plant]["rating"])
    if length == 0:
        plants[plant]["rating"] = 0
    else:
        total_sum = sum(plants[plant]["rating"])
        average = total_sum / length
        plants[plant]["rating"] = average

print("Plants for the exhibition:")

for key, value in plants.items():
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {value['rating']:.2f}")

