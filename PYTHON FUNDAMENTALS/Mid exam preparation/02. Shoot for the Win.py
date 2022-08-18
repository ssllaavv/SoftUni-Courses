customers = int(input())
wagons_state = input().split()

for i in range(len(wagons_state)):

    wagons_state[i] = int(wagons_state[i])

capacity = 4 * len(wagons_state)
free_places = capacity - sum(wagons_state)

for index in range(len(wagons_state)):
    while wagons_state[index] <= 3 and free_places >= 1 and customers >= 1:
        wagons_state[index] += 1
        customers -= 1
        free_places -= 1
if customers == 0 and free_places > 0:
    print("The lift has empty spots!")
    print(*wagons_state)
elif customers > 0:
    print(f"There isn't enough space! {customers} people in a queue!")
    print(*wagons_state)
elif customers == 0 and free_places == 0:
    print(*wagons_state)
