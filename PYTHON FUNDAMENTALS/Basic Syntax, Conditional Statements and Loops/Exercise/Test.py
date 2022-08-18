number = "123456789"

for index, value in enumerate(number):
    if int(value) % 2 == 0:
        print(index, value)