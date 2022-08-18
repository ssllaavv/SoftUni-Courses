def print_bool_if_palindrome(list_of_nums):
    for e in list_of_nums:
        original_num = e
        reversed_num = e[:: -1]
        if original_num == reversed_num:
            print("True")
        else:
            print("False")

llist_of_numbers = (input()).split(", ")
print_bool_if_palindrome(llist_of_numbers)
