def get_all_chars_inbetween(first_char, second_char):
    result_list = []
    for ch in range(ord(first_char) + 1, ord(second_char)):
        result_list.append(chr(ch))
    return result_list

first_input = input()
second_input = input()
result = get_all_chars_inbetween(first_input, second_input)
print(" ".join(result))
