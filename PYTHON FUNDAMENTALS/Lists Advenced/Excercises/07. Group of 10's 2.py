nums_row = input().split(", ")
list_of_all_nums = [int(el) for el in nums_row]

temp_group = 10
while len(list_of_all_nums) > 0:
    temp_list = [el for el in list_of_all_nums if el > (temp_group - 10)
                 and (el <= temp_group)]
    list_of_all_nums = [el for el in list_of_all_nums if el not in temp_list]
    print(f"Group of {temp_group}'s: {temp_list}")
    temp_list = []
    temp_group += 10
