text = (input()).upper()

current_text = ""
multiplier = ""
result = ""

for index in range(len(text)):
    if not text[index].isdigit():
        current_text += text[index]
    else:
        if multiplier == "":
            multiplier = text[index]
            if index == len(text) - 1:
                result += current_text * int(multiplier)
            else:
                if not text[index + 1].isdigit():
                    result += current_text * int(multiplier)
                    multiplier = ""
                    current_text = ""
        else:
            multiplier += text[index]
            result += current_text * int(multiplier)
            multiplier = ""
            current_text = ""

unique_chars = set(result)
print(f"Unique symbols used: {len(unique_chars)}")
print(result)
