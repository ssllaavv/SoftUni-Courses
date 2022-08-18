def check_if_num_is_palindrome(list_of_integers):
    for el in list_of_integers:
        if el == el[::-1]:
            print(True)
        else:
            print(False)


list_of_numbers = input().split(", ")
check_if_num_is_palindrome(list_of_integers=list_of_numbers)
