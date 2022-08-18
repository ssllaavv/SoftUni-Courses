import re

text = input()

valid_pairs = []
mirror_pairs = []
patten_pairs = r"(?P<Pairs>(?P<Sur>#|@)[A-Za-z]{3,}(?P=Sur)(?P=Sur)[A-Za-z]{3,}(?P=Sur))"

matches = re.finditer(patten_pairs, text)
for match in matches:
    valid_pairs.append(match.group("Pairs"))

if len(valid_pairs) == 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{len(valid_pairs)} word pairs found!")
    for pair in valid_pairs:
        len_of_word = int((len(pair) / 2) - 2)
        first_word = pair[1:len_of_word + 1]
        second_word = pair[len_of_word + 3: -1]
        if first_word == second_word[:: -1]:
            mirror_pairs.append(f"{first_word} <=> {second_word}")

    if len(mirror_pairs) == 0:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(", ".join(mirror_pairs))
