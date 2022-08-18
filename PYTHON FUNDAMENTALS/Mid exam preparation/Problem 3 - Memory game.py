pairs_of_elements = list(input().split())

guesses_count = 0
is_won = False

while True:
    guess = input().split()
    if guess == ["end"]:
        break

    guesses_count += 1
    first_index = int(guess[0])
    second_index = int(guess[1])
    if first_index in range(len(pairs_of_elements)) and second_index in range(len(pairs_of_elements)) and guess[0] != guess[1]:
        if pairs_of_elements[first_index] == pairs_of_elements[second_index]:
            element = pairs_of_elements.pop(first_index)
            pairs_of_elements.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print("Try again!")
    else:
        index = len(pairs_of_elements) // 2
        new_element = "-" + str(guesses_count) + "a"
        pairs_of_elements.insert(index, f"{new_element}")
        pairs_of_elements.insert(index, f"{new_element}")
        print("Invalid input! Adding additional elements to the board")

    if len(pairs_of_elements) == 0:
        is_won = 1
        break

if is_won:
    print(f"You have won in {guesses_count} turns!")
else:
    print("Sorry you lose :(")
    print(*pairs_of_elements)

