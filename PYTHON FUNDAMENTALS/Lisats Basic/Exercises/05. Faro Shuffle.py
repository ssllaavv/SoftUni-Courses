deck_original = input().split(" ")
shuffle_count = int(input())

result_list = []

for shuffle in range(shuffle_count):
    left_list = deck_original[:len(deck_original)//2]
    right_list = deck_original[len(deck_original)//2:]

    for element in range(len(deck_original)//2):
        result_list.append(left_list.pop(0))
        result_list.append(right_list.pop(0))
    deck_original = result_list
    result_list = []

print(deck_original)


