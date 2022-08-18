nums_row = input().split(", ")
list_of_all_nums = [int(el) for el in nums_row]

temp_group = 10
temp_list = []

while len(list_of_all_nums) > 0:
    for el in range(len(list_of_all_nums)):
        if el <= temp_group:
            temp_list.append(el)
            list_of_all_nums.remove(el)
    print(f"Group of {temp_group}'s: {temp_list}")
    temp_list.clear()
    temp_group += 10
