useful_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}
magic_item_obtained = False
magic_item = ""

while magic_item_obtained is False:
    input_line = input().split()
    for el in range(1, len(input_line) + 1, 2):
        if input_line[el].lower() in useful_materials:
            useful_materials[input_line[el].lower()] += int(input_line[el - 1])
        else:
            if input_line[el].lower() not in junk_materials:
                junk_materials[input_line[el].lower()] = int(input_line[el - 1])
            else:
                junk_materials[input_line[el].lower()] += int(input_line[el - 1])

        for key, value in useful_materials.items():
            if value >= 250:
                magic_item_obtained = True
                useful_materials[key] -= 250
                if key == "shards":
                    magic_item = "Shadowmourne"
                elif key == "fragments":
                    magic_item = "Valanyr"
                elif key == "motes":
                    magic_item = "Dragonwrath"
                break
        if magic_item_obtained:
            break

print(f"{magic_item} obtained!")

for key, value in useful_materials.items():
    print(f"{key}: {value}")
for key, value in junk_materials.items():
    print(f"{key}: {value}")