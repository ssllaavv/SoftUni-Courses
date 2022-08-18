fires_info = input().split("#")
water = int(input())

is_valid_data = False
total_fire = 0
effort = .25 * total_fire

print("Cells:")

for item in fires_info:
    current_cell = item.split(" = ")
    if current_cell[0] == "High":
        if int(current_cell[1]) in range(81, 125 + 1):
            if water >= int(current_cell[1]):
                water -= int(current_cell[1])
                total_fire += int(current_cell[1])
                print(f" - {int(current_cell[1])}")

    elif current_cell[0] == "Medium":
        if int(current_cell[1]) in range(51, 80 + 1):
            if water >= int(current_cell[1]):
                water -= int(current_cell[1])
                total_fire += int(current_cell[1])
                print(f" - {int(current_cell[1])}")

    elif current_cell[0] == "Low":
        if int(current_cell[1]) in range(1, 50 + 1):
            if water >= int(current_cell[1]):
                water -= int(current_cell[1])
                total_fire += int(current_cell[1])
                print(f" - {int(current_cell[1])}")
effort = .25 * total_fire

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")