text = input()
encrypted_text = ""

for letter in text:
    encrypted_text += chr(ord(letter) + 3)

print(encrypted_text)
