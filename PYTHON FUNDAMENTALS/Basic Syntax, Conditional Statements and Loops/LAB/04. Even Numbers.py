numbers = int(input())

for n in range(numbers):
    input_line = int(input())
    if input_line % 2 != 0:
        print(f"{input_line} is odd!")
        break
else:
    print(f"All numbers are even.")

