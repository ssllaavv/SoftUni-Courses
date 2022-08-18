force_side_dict = {}

to_change_sides = False
while True:
    input_line = input()
    if input_line == "Lumpawaroo":
        break
    if " | " in input_line:
        token = input_line.split(" | ")
        side, name = token
        if side not in force_side_dict:
            force_side_dict[side] = [name]
        else:
            for value in force_side_dict.values():
                if name not in force_side_dict.values():
                    force_side_dict[side] += [name]

    elif " -> " in input_line:
        token = input_line.split(" -> ")
        side,  name = token
        if side not in force_side_dict:
            force_side_dict[side] = [name]

        for key, value in force_side_dict.items():
            if name in value:
                force_side_dict[key].pop(value.index(name))
                to_change_sides = True

        else:
            force_side_dict[side] += [name]
        if to_change_sides:
            for k in force_side_dict.keys():
                if side != k:
                    force_side_dict[k] += [name]
            to_change_sides = False
        print(f"{name} joins the {side} side!")


for force_side, names in force_side_dict.items():
    if len(force_side_dict[force_side]) > 0:
        print(f"Side: {force_side}, Members: {len(names)}")
        for el in names:
            print(f"! {el}")
