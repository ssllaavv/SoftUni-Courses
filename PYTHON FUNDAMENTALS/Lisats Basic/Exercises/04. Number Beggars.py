donation_list = input().split(", ")
beggars_count = int(input())

result_list = []
int_of_donation_list = []

for value in donation_list:
    int_of_donation_list.append(int(value))

for beggar in range(1, beggars_count + 1):
    current_beggars_result = 0
    for element in range(beggar -1, len(int_of_donation_list), beggars_count):
        if element <= (len(int_of_donation_list)):
            current_beggars_result += int_of_donation_list[element]
    result_list.append(current_beggars_result)

print(result_list)