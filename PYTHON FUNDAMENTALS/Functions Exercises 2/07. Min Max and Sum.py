def print_min_maX_and_sum(list_of_some_integers):
    print(f"The minimum number is {min(list_of_some_integers)}")
    print(f"The maximum number is {max(list_of_some_integers)}")
    print(f"The sum number is: {sum(list_of_some_integers)}")

list_of_ints = list(map(int, input().split()))
print_min_maX_and_sum(list_of_ints)
