command = input()
coffees_count = 0
while command != "END":
    if command == "coding" or command == "movie" or command == "cat" or command == "dog":
        coffees_count += 1
    elif command == "CODING" or command == 'MOVIE' or command == "CAT" or command == "DOG":
        coffees_count += 2
    command = input()
if coffees_count > 5:
    print("You need extra sleep")
else:
    print(coffees_count)