cars_count = int(input())

cars = {}

for i in range(cars_count):
    input_line = input().split("|")
    name = input_line[0]
    mileage = int(input_line[1])
    fuel = int(input_line[2])
    cars[name] = {}
    cars[name]["mileage"] = mileage
    cars[name]["fuel"] = fuel

while True:
    line_input = input().split(" : ")
    command = line_input[0]
    if command == "Stop":
        break

    else:
        car = line_input[1]
        if command == "Drive":
            distance = int(line_input[2])
            fuel = int(line_input[3])
            if fuel > int(cars[car]["fuel"]):
                print("Not enough fuel to make that ride")
            else:
                cars[car]["mileage"] += distance
                cars[car]["fuel"] -= fuel
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                if cars[car]["mileage"] >= 100000:
                    del cars[car]
                    print(f"Time to sell the {car}!")
        if command == "Refuel":
            fuel = int(line_input[2])
            actual_fuel = fuel

            cars[car]["fuel"] += fuel
            diff = cars[car]["fuel"] - 75
            if diff > 0:
                actual_fuel = fuel - diff
                cars[car]["fuel"] = 75
            print(f"{car} refueled with {actual_fuel} liters")
        if command == "Revert":
            kilometers = int(line_input[2])
            cars[car]["mileage"] -= kilometers
            if cars[car]["mileage"] < 10000:
                cars[car]["mileage"] = 10000
            else:
                print(f"{car} mileage decreased by {kilometers} kilometers")

for car, value in cars.items():
    print(f'{car} -> Mileage: {value["mileage"]} kms, Fuel in the tank: {value["fuel"]} lt.')
