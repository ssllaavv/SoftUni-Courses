encoded_words = input().split()

first_letter_ord = ""
remaining_str = []
decoded_word = ""

for i in range(len(encoded_words)):
    for ch in encoded_words[i]:
        if ch.isdigit():
            first_letter_ord += ch
        else:
            remaining_str += ch
    if len(remaining_str) > 1:
        remaining_str_decoded = [remaining_str.pop()]
        last_char = remaining_str.pop(0)
        for letter in remaining_str:
            remaining_str_decoded.append(letter)
        remaining_str_decoded.append(last_char)
        decoded_remaining_as_str = "".join(remaining_str_decoded)
        decoded_word = chr(int(first_letter_ord)) + decoded_remaining_as_str
    else:
        decoded_word = chr(int(first_letter_ord)) + remaining_str[0]
    print(decoded_word, end=" ")
    first_letter_ord = ""
    remaining_str.clear()
    decoded_word = ""
    remaining_str_decoded.clear()

