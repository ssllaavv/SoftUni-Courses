number_list = list(map(int, input().split(", ")))

found_indexes_or_no = map(
    lambda x: x if number_list[x] % 2 == 0 else "no", range(len(number_list)))
result = list(filter(lambda x: x != "no", found_indexes_or_no))

print(result)
