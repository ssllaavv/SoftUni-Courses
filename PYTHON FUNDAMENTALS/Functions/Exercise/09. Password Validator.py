def check_pass_validity(entry):
    is_valid = True
    if not entry.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    if len(entry) < 6 or len(entry) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    counter = 0
    for symbol in entry:
        if symbol.isnumeric():
            counter += 1
    if counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")

password = input()
check_pass_validity(password)
