rooms_count = int(input())

current_room_data = []
free_chairs_count = 0
is_enough = True
for el in range(1, rooms_count + 1):
    current_room_data = input().split()
    diff = len(current_room_data[0]) - int(current_room_data[1])
    if diff >= 0:
        free_chairs_count += diff
    else:
        print(f"{abs(diff)} more chairs needed in room {el}")
        is_enough = False

if is_enough:
    print(f"Game On, {free_chairs_count} free chairs left")
