def print_tibonacci_seq(length):
    first_num = 0
    second_num = 0
    third_num = 0
    for n in range(1, length + 1):
        if n == 1 or n == 2:
            print(f"{1}", end=" ")
        elif n == 3:
            print(f"{2}", end=" ")
            first_num = 1
            second_num = 1
            third_num = 2
        else:
            current_num = first_num + second_num + third_num
            print(current_num, end=" ")
            first_num = second_num
            second_num = third_num
            third_num = current_num

count = int(input())
print_tibonacci_seq(count)
