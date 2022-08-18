year = int(input())

is_happy = False

while not is_happy:
    year += 1
    year_str = str(year)
    set_year = set()

    for digit in range(len(year_str)):
        set_year.add(year_str[digit])

    is_happy = len(set_year) == len(year_str)
    if is_happy:
        break
print(year)








