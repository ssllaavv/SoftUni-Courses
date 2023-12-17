import re

text = input()
pattern = r"(?P<Emoji>(?P<start_end>::|\*\*)[A-Z]{1}[a-z]{2,}(?P=start_end))"

threshold_list = re.findall(r"\d", text)
threshold = 1
for digit in threshold_list:
    threshold *= int(digit)

print(f"Cool threshold: {threshold}")
matches = re.finditer(pattern, text)

list_of_emojis = []

for match in matches:
    list_of_emojis.append(match.group("Emoji"))

print(f"{len(list_of_emojis)} emojis found in the text. The cool ones are:")

for emoji in list_of_emojis:
    coolness = 0
    for character in emoji[2:-2]:
        coolness += ord(character)
    if coolness >= threshold:
        print(emoji)

