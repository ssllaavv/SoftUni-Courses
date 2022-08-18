def print_odds_and_evens_sum(num):
    even_sum = 0
    odd_sum = 0
    for n in num:
        if int(n) % 2 == 0:
            even_sum += int(n)
        else:
            odd_sum += int(n)
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

number = input()
print_odds_and_evens_sum(number)

