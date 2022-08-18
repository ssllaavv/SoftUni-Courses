first_char = input()
second_char = input()

def ascii_chars_inbetween(chr_1, chr_2):
    ord_chr_1 = ord(chr_1)
    ord_chr_2 = ord(chr_2)
    list_of_chars = []
    for c in range(ord_chr_1 + 1, ord_chr_2):
        list_of_chars.append(chr(c))
    return list_of_chars
result = ascii_chars_inbetween(first_char, second_char)
print(" ".join(result))

