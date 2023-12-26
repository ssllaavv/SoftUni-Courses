# Task 1

numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    number = input()
    try:
        number = int(number)
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')
    line = input()

line = input()

while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print('Number does not exist in dictionary')
    line = input()

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print('Number does not exist in dictionary')
    line = input()

print(numbers_dictionary)


# Task 2

class NameTooShortError(Exception):
    """Name must be more than 4 characters"""
    pass


class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass


while True:
    email = input()
    if email == 'End':
        break

    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @"')

    at_index = email.index('@')
    name = email[: at_index]
    if len(name) < 4:
        raise NameTooShortError('Name must be more than 4 characters')

    reversed_email = ''.join(list(reversed(email)))
    if reversed_email[: 4] == 'moc.' or \
            reversed_email[: 3] == 'gb.' or \
            reversed_email[: 4] == 'gro.' or \
            reversed_email[: 4] == 'ten.':
        print('Email is valid')
    else:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
