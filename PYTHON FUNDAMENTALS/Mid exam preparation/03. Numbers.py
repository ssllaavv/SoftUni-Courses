input_list = input().split()

for index in range(len(input_list)):
    input_list[index] = int(input_list[index])

average = sum(input_list) / len(input_list)
input_list.sort(reverse=True)

if input_list[0] <= average:
    print("No")
else:
    counter = 0
    for number in input_list:
        if number > average and counter < 5:
            counter += 1
            print(number, end=" ")
