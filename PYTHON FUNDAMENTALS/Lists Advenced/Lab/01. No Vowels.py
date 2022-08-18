string_input = input()

vowels_list = ["a", "e", "i", "o", "u"]

new_string = [el for el in string_input if el.lower() not in vowels_list]

print("".join(new_string))

