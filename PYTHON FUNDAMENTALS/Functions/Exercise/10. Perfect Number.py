def check_if_number_is_perfect(some_number):
    sum_to_check = 0
    is_perfect_number = False
    for n in range(1, some_number):
        if some_number % n == 0:
            sum_to_check += n
        if sum_to_check == some_number:
            print("We have a perfect number!")
            is_perfect_number = True
            break
    if not is_perfect_number:
        print("It's not so perfect.")

number = int(input())
check_if_number_is_perfect(number)
