numbers = input().split(", ")
list_of_nums = [int(num) for num in numbers]
positives = [num for num in list_of_nums if num >= 0]
negatives = [num for num in list_of_nums if num < 0]
evens = [num for num in list_of_nums if num % 2 == 0]
odds = [num for num in list_of_nums if num % 2 != 0]

print("Positive:", end=' ')
print(*positives, sep=', ')
print("Negative:", end=' ')
print(*negatives, sep=', ')
print("Even:", end=' ')
print(*evens, sep=', ')
print("Odd:", end=' ')
print(*odds, sep=', ')

