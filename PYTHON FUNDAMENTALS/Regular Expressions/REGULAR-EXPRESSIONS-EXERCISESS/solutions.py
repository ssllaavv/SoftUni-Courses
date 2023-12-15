# Task 1
import re

text = ''
line = input()

while line:
    text += f'\n{line}'
    line = input()

pattern = r'\d+'
matches = re.findall(pattern, text)
print(' '.join(matches))


# Task 2
import re

text = input()
pattern = r'(?<=\b_)([a-z]+|[A-Z]+|[\d]+)+\b'
matches = [match.group() for match in re.finditer(pattern, text)]

print(','.join(matches))


# Task 3
import re

text = input().lower()
word = input().lower()
pattern = f'\\b{word}\\b'

matches = re.findall(pattern, text)

print(len(matches))


# Task 4
import re

text = input()
pattern = r'((?<=(\s))|^)([a-zA-Z]+|\d+)+((\.|\-|\_){1}([a-zA-Z]+|\d+)+)*' \
          r'@([a-zA-Z]+|\d+)+(\-([a-zA-Z]+|\d+)+)*' \
          r'(\.([a-zA-Z]+|\d+)+(\-([a-zA-Z]+|\d+)+)*)+'

matches = [match.group() for match in re.finditer(pattern, text)]

for match in matches:
    print(match)



# Task 5
import re

text = ''
while True:
    line = input()
    if line == 'Purchase':
        break
    text += f'\n{line}'

pattern = r'>>(?P<furniture>[^<]+)<<(?P<price>[0]|[1-9]\d*(\.\d+)*)!(?P<qtt>\d+)'
matches = [match.groupdict() for match in re.finditer(pattern, text)]

total_bill = 0

print('Bought furniture:')
for match in matches:
    print(match['furniture'])
    total_bill += int(match['qtt']) * float(match['price'])

print(f'Total money spend: {total_bill:.2f}')


# Task 6
import re

text = ""

line = input()
while line:
    text += f'\n{line}'
    line = input()

pattern = r'\bwww\.(\d|[a-zA-Z])+(\-(\d|[a-zA-Z])+)*(\.[a-z]+)+'
matches = [match.group() for match in re.finditer(pattern, text)]

print('\n'.join(matches))


















