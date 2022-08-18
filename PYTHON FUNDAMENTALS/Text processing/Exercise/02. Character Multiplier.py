first_word, second_word = input().split()
final_result = 0

diff = (len(first_word) - len(second_word))
if diff > 0:
    second_word += chr(1) * diff
else:
    first_word += chr(1) * abs(diff)

for index in range(len(first_word)):
    current_result = ord(first_word[index]) * ord(second_word[index])
    final_result += current_result
    current_result = 0
print(final_result)





