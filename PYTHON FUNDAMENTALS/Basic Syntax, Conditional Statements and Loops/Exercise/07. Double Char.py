string = input()
doubled_string = ""

while string != "End":
    if string == "SoftUni":
        string = input()
        continue
    for char in string:
        doubled_string += 2 * char
    print(doubled_string)
    doubled_string = ""
    string = input()



