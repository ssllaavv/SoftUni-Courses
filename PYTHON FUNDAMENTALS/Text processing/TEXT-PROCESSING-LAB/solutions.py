# Task 1

while True:
    text = input()
    if text == 'end':
        break
    reversed_text = ''.join(list(reversed(text)))
    print(f'{text} = {reversed_text}')


# Task 2

strings = input().split(' ')
result = ''

for s in strings:
    result += s * len(s)

print(result)



# Task 3

word = input()
sentence = input()

while word in sentence:
    sentence = sentence.replace(word, '')

print(sentence)



# Task 4

banned_words = input().split(', ')
text = input()

for word in banned_words:
    text = text.replace(word, '*' * len(word))

print(text)


# Task 5

text = input()

digits = ''
letters = ''
symbols = ''

for l in text:
    if l.isdigit():
        digits += l
    elif l.isalpha():
        letters += l
    else:
        symbols += l
        symbols.strip()

print(digits)
print(letters)
print(symbols)














