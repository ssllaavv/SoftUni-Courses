# Task 1

input_line = input().split(' ')

bakery = dict()

for i in range(0, len(input_line), 2):
    bakery[input_line[i]] = int(input_line[i + 1])

print(bakery)



# Task 2

inputs = input().split(' ')

products = {}
for i in range(0, len(inputs), 2):
    products[inputs[i]] = int(inputs[i + 1])

queries = input().split(' ')

for q in queries:
    if q in products:
        print(f"We have {products[q]} of {q} left")
    else:
        print(f"Sorry, we don't have {q}")


# Task 3

products = {}

while True:
    command = input().split(': ')
    if command[0] == 'statistics':
        break

    product, quantity = command
    if product not in products:
        products[product] = int(quantity)
    else:
        products[product] += int(quantity)

count_all_products = len(products.keys())
sum_all_quantities = sum(products.values())

products_string = [f"- {key}: {value}" for key, value in products.items()]

print("Products in stock:")
print('\n'.join(products_string))
print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_all_quantities}")




# Task 5

letters = input().split(', ')

ascii_dict = {l: ord(l) for l in letters}

print(ascii_dict)


# Task 6

words = input().split(' ')
words_dict = {}
odd_words = []

for word in words:
    lower_word = word.lower()
    if lower_word not in words_dict:
        words_dict[lower_word] = 0
    words_dict[lower_word] += 1

for k, v in words_dict.items():
    if v % 2 == 1:
        odd_words.append(k)

print(' '.join(odd_words))


# Task 7

n = int(input())
all_words = []
words_synonyms = {}


for i in range(n):
    word = input()
    synonym = input()
    if word not in words_synonyms:
        words_synonyms[word] = []
    words_synonyms[word].append(synonym)

for word, synonyms in words_synonyms.items():
    print(f'{word} - {", ".join(synonyms)}')





















