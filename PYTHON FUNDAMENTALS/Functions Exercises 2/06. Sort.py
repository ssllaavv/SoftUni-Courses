def print_in_ascending_order(some_list_of_ints):
    print(sorted(some_list_of_ints))

list_of_ints = list(map(int, input().split()))
print_in_ascending_order(list_of_ints)

