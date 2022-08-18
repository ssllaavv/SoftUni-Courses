text = input()
for index in range(len(text)):
    if text[index] == ":" and text[index + 1] != " ":
        print(f":{text[index + 1]}")


