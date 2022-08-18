def check_pass_validity(password):
    is_valid = True
    if len(password) > 10 or len(password) < 6:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")
    digits_counter = 0
    for character in password:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")

input_pass = input()
check_pass_validity(input_pass)


