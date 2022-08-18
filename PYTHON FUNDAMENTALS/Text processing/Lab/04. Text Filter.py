banned_list = input().split(", ")
text = input()

for el in banned_list:
    while el in text:
        text = text.replace(el, "*" * len(el))

print(text)


