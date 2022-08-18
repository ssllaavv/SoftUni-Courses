import re

text = input()
cool_emojis = []
threshold = 1

pattern_emoji = r"(::[A-Z]{1}[a-z]{2}[a-z]*::)|(\*\*[A-Z]{1}[a-z]{2}[a-z]*\*\*)"
pattern_digits = r"\d{1}"

result = re.finditer(pattern_emoji, text)

matches_emoji = []
for match in result:
    matches_emoji.append(match.group())

""" 
matches_emoji_raw = re.findall(pattern_emoji, text)

matches_emoji = []
for tup in matches_emoji_raw:
    for el in tup:
        if el != "":
            matches_emoji.append(el)
"""
emojis_count = len(matches_emoji)

matches_digits = re.findall(pattern_digits, text)

for digit in matches_digits:
    threshold *= int(digit)


for i in range(len(matches_emoji)):
    coolness = 0
    stripped_emoji = (matches_emoji[i])[2:-2]
    for char in stripped_emoji:
        coolness += ord(char)
    if coolness >= threshold:
        cool_emojis.append(matches_emoji[i])

print(f"Cool threshold: {threshold}")
print(f"{emojis_count} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)
