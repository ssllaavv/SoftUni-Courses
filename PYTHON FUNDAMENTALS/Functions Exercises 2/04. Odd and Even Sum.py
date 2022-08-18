def get_sum_of_evens_and_sum_of_odds(some_integer):
    even_sum = 0
    odd_sum = 0
    for el in some_integer:
        if int(el) % 2 == 0:
            even_sum += int(el)
        else:
            odd_sum += int(el)
    result = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return result

input_number = input()
result = get_sum_of_evens_and_sum_of_odds(input_number)
print(result)
