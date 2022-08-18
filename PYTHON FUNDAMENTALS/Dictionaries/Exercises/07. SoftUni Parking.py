commands_count = int(input())
parked_cars = {}
for cmd in range(commands_count):
    input_line = input().split()
    name = input_line[1]
    if input_line[0] == "register":
        plate = input_line[2]
        if name in parked_cars:
            print(f"ERROR: already registered with plate number {plate}")
        else:
            parked_cars[name] = plate
            print(f"{name} registered {plate} successfully")
    elif input_line[0] == "unregister":
        if name not in parked_cars:
            print(f"ERROR: user {name} not found")
        else:
            parked_cars.pop(name)
            print(f"{name} unregistered successfully")

for name, plate in parked_cars.items():
    print(f"{name} => {plate}")