list_of_nums = input().split()

for i in range(len(list_of_nums)):
    list_of_nums[i] = int(list_of_nums[i])

removed_number = int()
sum_of_removed = int()

while len(list_of_nums) >= 1:
    index = int(input())
    if (index >= 0) and index <= (len(list_of_nums) - 1):
        removed_number = list_of_nums.pop(index)
    elif index < 0:
        removed_number = list_of_nums.pop(0)
        if len(list_of_nums) >= 1:
            list_of_nums.insert(0, list_of_nums[-1])
        else:
            continue
    elif index > len(list_of_nums) - 1:
        removed_number = list_of_nums.pop(-1)
        if len(list_of_nums) >= 1:
            list_of_nums.append(list_of_nums[0])
        else:
            continue
    sum_of_removed += removed_number

    for idx in range(len(list_of_nums)):
        if list_of_nums[idx] <= removed_number:
            list_of_nums[idx] += removed_number
        else:
            list_of_nums[idx] -= removed_number

print(sum_of_removed)
