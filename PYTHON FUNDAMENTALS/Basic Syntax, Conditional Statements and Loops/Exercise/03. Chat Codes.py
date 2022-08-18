numbers_count = int(input())

for n in range(numbers_count):
    number = int(input())
    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number < 88:
        print("GREAT!")
    elif number > 88:
        print("Bye.")
