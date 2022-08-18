first_list = input().split(", ")
second_list = input().split(", ")

result_list = [first_word for first_word in first_list if any(first_word in second_word for second_word in second_list)]

print(result_list)
