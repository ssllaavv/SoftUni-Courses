to_remove_str = input()
text = input()

while to_remove_str in text:
    text = text.replace(to_remove_str, "")

print(text)
