list_of_cards = input().split(", ")
commands_count = int(input())

for n in range(commands_count):
    command = input().split(", ")
    if command[0] == "Add":
        card_name = command[1]
        if card_name in list_of_cards:
            print("Card is already in the deck")
        else:
            list_of_cards.append(card_name)
            print("Card successfully added")
    elif command[0] == "Remove":
        card_name = command[1]
        if card_name in list_of_cards:
            list_of_cards.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif command[0] == "Remove At":
        index = int(command[1])
        if index in range(len(list_of_cards)):
            list_of_cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif command[0] == "Insert":
        index = int(command[1])
        card_name = command[2]
        if index not in range(len(list_of_cards)):
            print("Index out of range")
        else:
            if card_name in list_of_cards:
                print("Card is already added")
            else:
                list_of_cards.insert(index, card_name)
                print("Card successfully added")

print(*list_of_cards, sep=", ")