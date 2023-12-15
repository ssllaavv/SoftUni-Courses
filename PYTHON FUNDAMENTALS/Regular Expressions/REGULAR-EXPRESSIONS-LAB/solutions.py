
# Task 1
import re

text = input()
pattern = r'\b[A-Z]{1}[a-z]+\b\s\b[A-Z]{1}[a-z]+\b'

all_matches = re.findall(pattern, text)

print(' '.join(all_matches))


# Task 2
import re

text = input()
pattern = r'\+359([ -])2\1\d{3}\1\d{4}\b'
all_matches = list(re.finditer(pattern, text))

print(', '.join([match.group() for match in all_matches]))


# Task 3

import re

text = input()
pattern = r'\b(?P<day>\d{2})(?P<separator>[-/.])(?P<month>[A-Z]{1}[a-z]{2})(?P=separator)(?P<year>\d{4})\b'

matches = [match.groupdict() for match in re.finditer(pattern, text)]

for el in matches:
    print(f'Day: {el["day"]}, Month: {el["month"]}, Year: {el["year"]}')



# Task 4

import re

text = input()
pattern = r'(^|(?<=\s))-?(0|[1-9]\d*)(\.\d+)?($|(?=\s))'

matches = [match.group() for match in re.finditer(pattern, text)]

print(' '.join(matches))



















