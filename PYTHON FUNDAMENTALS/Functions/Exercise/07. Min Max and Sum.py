def print_min_max_sum(some_list):
    min_num = min(some_list)
    max_num = max(some_list)
    sum_of_nums = sum(some_list)
    print(f"The minimum number is {min_num}")
    print(f"The maximum number is {max_num}")
    print(f"The sum number is: {sum_of_nums}")


numbers_as_strings_list = input().split()
numbers_as_ints_list = []
for e in numbers_as_strings_list:
    numbers_as_ints_list.append(int(e))
print_min_max_sum(numbers_as_ints_list)




